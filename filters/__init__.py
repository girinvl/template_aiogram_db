from filters.is_approved import IsApproved
from loader import dp
# from .is_admin import AdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(IsApproved)
    # dp.filters_factory.bind(AdminFilter)
