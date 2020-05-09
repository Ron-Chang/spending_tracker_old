

class ACTIVITY_TYPE:
    """
    末位 0 登出 註銷 刪除
    末位 1 登入 註冊 新增
    末位 2 更新 修改 編輯
    """

    LOGOUT = 0
    LOGIN = 1

    ACCOUNT_DELETE = 100  # 註銷帳戶
    ACCOUNT_SIGNUP = 101  # 註冊帳戶
    ACCOUNT_UPDATE = 102  # 更新帳戶
    SHEET_DELETE = 200  # 刪除記帳簿
    SHEET_CREATE = 201  # 新增記帳簿
    SHEET_MODIFY = 202  # 編輯記帳簿
    BALANCE_DELETE = 300  # 刪除記帳內容
    BALANCE_CREATE = 301  # 新增記帳內容
    BALANCE_MODIFY = 302  # 修改記帳內容

    ERROR = 999  # 錯誤

    _MAP_TITLE = {
        LOGOUT: 'logout',
        LOGIN: 'login',
        ACCOUNT_DELETE: 'delete-account',
        ACCOUNT_SIGNUP: 'signup-account',
        ACCOUNT_UPDATE: 'update-account',
        SHEET_DELETE: 'delete-sheet',
        SHEET_CREATE: 'create-sheet',
        SHEET_MODIFY: 'modify-sheet',
        BALANCE_DELETE: 'delete-balance',
        BALANCE_CREATE: 'create-balance',
        BALANCE_MODIFY: 'modify-balance',
        ERROR: 'error',
    }

    @classmethod
    def trans_title(cls, activity_type):
        return cls._MAP_TITLE.get(activity_type) or cls._MAP_TITLE.get(cls.ERROR)


if __name__ == '__main__':
    activity_type = ACTIVITY_TYPE.CREATE_BALANCE
    print(activity_type)
    activity = ACTIVITY_TYPE.trans_title(activity_type=333)
    print(activity)
