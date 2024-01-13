import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models
import timm
from timm.loss import LabelSmoothingCrossEntropy

class MultiOutputModel(nn.Module):
    def __init__(self, n_EXP_classes, n_ICM_classes, n_TE_classes):
        super().__init__()
        self.base_model = models.mobilenet_v2(pretrained=False).features  # take the model without classifier
        last_channel = models.mobilenet_v2().last_channel  # size of the layer before classifier
        self.pool = nn.AdaptiveAvgPool2d((1, 1))
        self.EXP = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(in_features=last_channel, out_features=n_EXP_classes)
        )
        self.ICM = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(in_features=last_channel, out_features=n_ICM_classes)
        )
        self.TE = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(in_features=last_channel, out_features=n_TE_classes)
        )

    def forward(self, x):
        x = self.base_model(x)
        x = self.pool(x)
        x = torch.flatten(x, 1)
        #print(x.size())
        return {
            'EXP': self.EXP(x),
            'ICM': self.ICM(x),
            'TE': self.TE(x)
        }

    def get_loss(self, net_output, ground_truth):        
        EXP_loss = F.cross_entropy(net_output['EXP'], ground_truth['EXP_labels'])
        ICM_loss = F.cross_entropy(net_output['ICM'], ground_truth['ICM_labels'])
        TE_loss = F.cross_entropy(net_output['TE'], ground_truth['TE_labels'])
        return EXP_loss,ICM_loss,TE_loss

    def get_loss_weighted(self, net_output, ground_truth,EXP_weights,ICM_weights,TE_weights):        
        EXP_loss = F.cross_entropy(net_output['EXP'], ground_truth['EXP_labels'])
        ICM_loss = F.cross_entropy(net_output['ICM'], ground_truth['ICM_labels'],ICM_weights)
        TE_loss = F.cross_entropy(net_output['TE'], ground_truth['TE_labels'],TE_weights)
        return EXP_loss,ICM_loss,TE_loss