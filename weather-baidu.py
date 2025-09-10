# encoding:utf-8
# import requests
import httpx
import json
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather", log_level="ERROR")#必须，不然可能会运行失败，因为mcp在运行时会输出很多日志

# 接口地址
url = "https://api.map.baidu.com/weather/v1/"
# 此处填写你在控制台-应用管理-创建应用后获取的AK
ak = "百度的 api key"

@mcp.tool()
async def get_forecast(district_id: str) -> str:
    """Get weather forecast for 一个城市的行政区域编号，百度地图官方定义的.

    Args:
        district_id: 百度地图官方定义的行政区域编号
    """
    if not district_id:
        return "请输入行政区域编号"


    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{url}?district_id={district_id}&data_type=all&ak={ak}")
            response.raise_for_status()
            data = response.json()
            return json.dumps(data)
        except Exception:
            return "请求失败"
        

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
