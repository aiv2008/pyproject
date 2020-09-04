import torch

def infoEntropy(X,x,In='bit')->torch.Tensor:
    n = torch.Tensor([X.shape[0]])
    px = torch.sum(X==x)/n
    if In == 'bit':
        return -px*torch.log2(px)
    elif In == 'nat':
        return -px*torch.log(px)
infoEntropy(x,x[1],'nat')

def infoEntropys(X,In='bit')->torch.Tensor:
    entropy_i = torch.Tensor([infoEntropy(X,x)[0] for x in X])
    return {'entropy':np.unique(entropy_i).sum(),'probability':{x:p for x,p in zip(X.numpy(),entropy_i)}}
infoEntropys(x)
