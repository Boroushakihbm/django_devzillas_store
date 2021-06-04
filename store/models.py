from .abstract_models import department
from .abstract_models import feature

__all__ = []


class Department(department.AbstractDepartment):
    pass


__all__.append('Department')


class Feature(feature.AbstractFeature):
    pass


__all__.append('Feature')
