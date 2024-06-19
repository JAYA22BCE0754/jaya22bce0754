import numpy as np

def calculator(list):
    if len(list)!=9:
        return ValueError("List must contain nine numbers.")
    x=np.array(list).reshape(3,3)
    print(x)
    print(np.sum(x,axis=0))
    cal={"mean":[np.mean(x,axis=0).tolist(),np.mean(x,axis=1).tolist(),np.mean(x)],"var":[np.var(x,axis=0).tolist(),np.var(x,axis=1).tolist(),np.var(x)],"standard deviation":[np.std(x,axis=0).tolist(),np.std(x,axis=1).tolist(),np.std(x)],"max":[np.max(x,axis=0).tolist(),np.max(x,axis=1).tolist(),np.max(x)],"min":[np.min(x,axis=0).tolist(),np.min(x,axis=1).tolist(),np.min(x)],"sum":[np.sum(x,axis=0).tolist(),np.sum(x,axis=1).tolist(),np.sum(x)]
    }
    return cal
