from .AllocModel import AllocModel
from .hmm.FiniteHMM import FiniteHMM
from .hmm.HDPHMM import HDPHMM
from .mix.DPMixtureModel import DPMixtureModel
from .mix.FiniteMixtureModel import FiniteMixtureModel
from .relational.FiniteAssortativeMMSB import FiniteAssortativeMMSB
from .relational.FiniteMMSB import FiniteMMSB
from .relational.FiniteSMSB import FiniteSMSB
from .relational.HDPAssortativeMMSB import HDPAssortativeMMSB
from .relational.HDPMMSB import HDPMMSB
from .topics.FiniteTopicModel import FiniteTopicModel
from .topics.HDPTopicModel import HDPTopicModel

AllocModelConstructorsByName = {
    'FiniteMixtureModel': FiniteMixtureModel,
    'DPMixtureModel': DPMixtureModel,
    'FiniteTopicModel': FiniteTopicModel,
    'HDPTopicModel': HDPTopicModel,
    'FiniteHMM': FiniteHMM,
    'HDPHMM': HDPHMM,
    'FiniteSMSB': FiniteSMSB,
    'FiniteMMSB': FiniteMMSB,
    'FiniteAssortativeMMSB': FiniteAssortativeMMSB,
    'HDPMMSB': HDPMMSB,
    'HDPAssortativeMMSB': HDPAssortativeMMSB,
}

AllocModelNameSet = set(AllocModelConstructorsByName.keys())

__all__ = ['AllocModel']
for name in AllocModelConstructorsByName:
    __all__.append(name)
