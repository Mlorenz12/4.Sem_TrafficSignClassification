from model.trafficSignsClassification import Model

# --- Change some parameters here ---
parameters = {"batchSize":50, "epochs":16, "validation":0.2}

# --- trains the network
model = Model(parameters)
model.trainModel()

