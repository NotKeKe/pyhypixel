from aiohttp import ClientResponse

class HypixelAPIError(Exception): pass
class BadRequest(HypixelAPIError): pass         # 400
class Forbidden(HypixelAPIError): pass          # 403
class TooManyRequests(HypixelAPIError): pass    # 429
class NotFound(HypixelAPIError): pass           # 404
class ServiceUnavailable(HypixelAPIError): pass # 503

def req_error(response: ClientResponse):
    if response.status == 200:
        return True
    elif response.status == 400:
        raise BadRequest("UUID 或參數缺失")
    elif response.status == 403:
        raise Forbidden("API 金鑰錯誤或權限不足")
    elif response.status == 429:
        wait_time = response.headers.get("RateLimit-Reset", "未知")
        raise TooManyRequests(f"速率限制已達上限，請等待 {wait_time} 秒")
    elif response.status == 404:
        raise NotFound("指定頁面不存在")
    elif response.status == 503:
        raise ServiceUnavailable("伺服器暫時無法使用，請稍候再試")
    else:
        raise HypixelAPIError(f"未預期的錯誤（HTTP {response.status}）")