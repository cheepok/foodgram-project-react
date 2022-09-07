DATE_TIME_FORMAT = '%d/%m/%Y %H:%M'

ADD_METHODS = ('GET', 'POST',)

DEL_METHODS = ('DELETE',)

ACTION_METHODS = [s.lower() for s in (ADD_METHODS + DEL_METHODS)]

UPDATE_METHODS = ('PUT', 'PATCH')

SEARCH_ING_NAME = 'name'

FAVORITE = 'is_favorited'

SHOP_CART = 'is_in_shopping_cart'

AUTHOR = 'author'

TAGS = 'tags'

SYMBOL_TRUE_SEARCH = ('1', 'true',)

SYMBOL_FALSE_SEARCH = ('0', 'false',)

SUBSCRIBE_M2M = 'subscribe'

FAVORITE_M2M = 'favorite'

SHOP_CART_M2M = 'shopping_cart'

MAX_LEN_USERS_CHARFIELD = 100

MIN_USERNAME_LENGTH = 3

MAX_LEN_EMAIL_FIELD = 50

MAX_LEN_RECIPES_CHARFIELD = 200

MAX_LEN_RECIPES_TEXTFIELD = 5000

USERS_HELP_EMAIL = ('Обязательно. До 50 символов.')

USERS_HELP_UNAME = ('Обязательно. От 3 до 100 символов.')

USERS_HELP_FNAME = ('Обязательно. До 100 символов.')
