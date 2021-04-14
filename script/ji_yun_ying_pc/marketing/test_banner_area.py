import allure
import pytest
import jsonpath
from common.operation_time import GetTime
from script.base_api.api_operation_web.banner import banner_area_query_post
from script.base_api.api_operation_web.banner import banner_area_add_post
from script.base_api.api_operation_web.banner import banner_area_changeStatus_get
from script.base_api.api_jksxb_mini.banner import banner_display_post
from script.ji_yun_ying_pc.marketing.data_config import banner_area_data
from script import public_asserts
from script.default_header import jyy_header,gos_header


@allure.feature("测试区域广告")
class TestBannerArea:

    @allure.story("测试区域广告查询-筛选")
    @pytest.mark.parametrize("area", banner_area_data.areas)
    @pytest.mark.parametrize("platform", banner_area_data.platform)
    @pytest.mark.parametrize("status", banner_area_data.status)
    def test_banner_area_list_search(self, area, platform, status):
        area_value = area.get("area_data")
        platform_value = platform.get("platform_type")
        status_value = status.get("status")
        body = {
            "title": "",
            "platform": platform_value,
            "locationLabel": "HOME",
            "areaIds": area_value,
            "status": status_value,
            "pageNum": 1,
            "pageSize": 10
        }
        res = banner_area_query_post(body=body, header=jyy_header)
        print(res)
        data_list_json = jsonpath.jsonpath(res, "$.data.list")
        if data_list_json:
            data_list = data_list_json[0]
            if len(data_list) > 0:
                platforms = jsonpath.jsonpath(res, "$.data.list..platform")
                result1 = public_asserts.assert_res_field_equal_value(platforms, platform_value)
                pytest.assume(result1)
                banner_status = jsonpath.jsonpath(res, "$.data.list..status")
                result2 = public_asserts.assert_res_field_equal_value(banner_status, status_value)
                pytest.assume(result2)
                banner_area_infos = jsonpath.jsonpath(res, "$.data.list..areaInfos")
                if banner_area_infos:
                    for banner_area_info_arr in banner_area_infos:
                        if banner_area_info_arr:
                            banner_area_info = banner_area_info_arr[0]
                            banner_area = banner_area_info["areaId"]
                            result3 = banner_area in area_value
                            pytest.assume(result3)

    @allure.story("测试区域广告新增")
    def test_banner_area_add(self):
        current_time = GetTime.get_current_time_millis()
        body = {
                "title": "接口自动化测试区域广告" + str(current_time),
                "platform": "APPLET",
                "locationLabel": "HOME",
                "odr": 1,
                "areaIds": [3014],
                "url": "www.baidu.com",
                "bannerInfos": [
                    {
                        "type": "IMAGE",
                        "value": "https://test-1257124244.image.myqcloud.com/gosGoodsImage/image/0f3cbef1-dfd2-4620-90e5-9fb87d1ef7bc.jpeg"
                     }
                ]
        }
        res = banner_area_add_post(body=body, header=jyy_header)
        print(res)
        public_asserts.public_assert(res)

    @allure.story("测试区域广告停用/启用及停用启用后的效果")
    @pytest.mark.parametrize("platform", banner_area_data.platform)
    def test_banner_area_enable(self, platform):
        platform_value = platform.get("platform_type")
        # 新增一个区域广告
        current_time = GetTime.get_current_time_millis()
        add_banner_body = {
            "title": "接口自动化测试区域广告" + str(current_time),
            "platform": platform_value,
            "locationLabel": "HOME",
            "odr": 1,
            "areaIds": [3014],
            "url": "www.baidu.com",
            "bannerInfos": [
                {
                    "type": "IMAGE",
                    "value": "https://test-1257124244.image.myqcloud.com/gosGoodsImage/image/0f3cbef1-dfd2-4620-90e5-9fb87d1ef7bc.jpeg"
                }
            ]
        }
        res_add_banner = banner_area_add_post(body=add_banner_body, header=jyy_header)
        public_asserts.public_assert(res_add_banner)
        # 获取新增的区域广告ID
        query_banner_body = {
            "title": add_banner_body["title"],
            "platform": add_banner_body["platform"],
            "locationLabel": "HOME",
            "status": "ENABLED",
            "pageNum": 1,
            "pageSize": 10
        }
        res_query_banner = banner_area_query_post(body=query_banner_body, header=jyy_header)
        public_asserts.public_assert(res_query_banner)
        print(res_query_banner)
        data_list_json = jsonpath.jsonpath(res_query_banner, "$.data.list")
        data_list = data_list_json[0]
        if len(data_list) > 0:
            banner_ids = jsonpath.jsonpath(res_query_banner, "$.data.list..id")
            if banner_ids:
                banner_id = str(banner_ids[0])
                # 停用新增的区域广告
                disable_param = "id=" + banner_id + "&status=DISABLED"
                res_changestaus = banner_area_changeStatus_get(params=disable_param, header=jyy_header)
                print(res_changestaus)
                public_asserts.public_assert(res_changestaus)
                query_banner_body = {
                    "locationLabel": "HOME",
                    "areaIds": [3014],
                }
                if platform_value == "APPLET":
                    # 小程序是否能查询到停用的区域广告
                    query_banner_body["platform"] = "APPLET"
                    res_banner_applet = banner_display_post(body=query_banner_body, header=gos_header)
                    display_banners_applet_ids = jsonpath.jsonpath(res_banner_applet, "$.data.displayBanners..id")
                    if display_banners_applet_ids:
                        result = int(banner_id) in display_banners_applet_ids
                        pytest.assume(not result)
                    print(res_banner_applet)
                else:
                    # 家长APP是否能查询到停用的区域广告
                    query_banner_body["platform"] = "APP"
                    res_banner_app = banner_display_post(body=query_banner_body, header=gos_header)
                    display_banners_app_ids = jsonpath.jsonpath(res_banner_app, "$.data.displayBanners..id")
                    if display_banners_app_ids:
                        result = int(banner_id) in display_banners_app_ids
                        pytest.assume(not result)
                    print(res_banner_app)
