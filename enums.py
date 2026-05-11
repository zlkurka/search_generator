from enum import Enum

class EnumWithValueRepr(Enum):
    def __repr__(self):
        return self.value
    
    def __str__(self):
        return self.value

class Category(EnumWithValueRepr):

    # Interventions
    dbt = "DBT"
    act = "ACT"

    # Outcomes
    depression = "Depression"
    anxiety = "Anxiety"
    self_injury = "Self-injury"

    # Populations
    lgbt = "LGBT"
    undocumented = "Undocumented"
    children = "Children"