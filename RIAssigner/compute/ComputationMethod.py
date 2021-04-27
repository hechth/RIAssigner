from abc import ABC, abstractmethod
from typing import List
from RIAssigner.data import Data


class ComputationMethod(ABC):

    @abstractmethod
    def compute(self, query: Data, reference: Data) -> List[float]:
        ...

    def _check_data_args(self, query, reference):
        assert query is not None, "Query data is 'None'."
        assert reference is not None, "Reference data is 'None'."
