class AttributesDataset():
    def __init__(self):
        # hardcoded unique labels
        self.EXP_labels = ['0', '1', '2', '3', '4']  # replace with your unique EXP labels
        self.ICM_labels = ['0', '1', '2', '3']  # replace with your unique ICM labels
        self.TE_labels = ['0', '1', '2', '3']  # replace with your unique TE labels

        self.num_EXPs = len(self.EXP_labels)
        self.num_ICMs = len(self.ICM_labels)
        self.num_TEs = len(self.TE_labels)

        self.EXP_id_to_name = dict(zip(range(len(self.EXP_labels)), self.EXP_labels))
        self.EXP_name_to_id = dict(zip(self.EXP_labels, range(len(self.EXP_labels))))

        self.ICM_id_to_name = dict(zip(range(len(self.ICM_labels)), self.ICM_labels))
        self.ICM_name_to_id = dict(zip(self.ICM_labels, range(len(self.ICM_labels))))

        self.TE_id_to_name = dict(zip(range(len(self.TE_labels)), self.TE_labels))
        self.TE_name_to_id = dict(zip(self.TE_labels, range(len(self.TE_labels))))

