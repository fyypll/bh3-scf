# settings
import logging

import os

__all__ = ['log', 'CONFIG']

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S')

log = logger = logging


class _Config:
    ACT_ID = 'ea20211026151532'
    APP_VERSION = '2.17.1'
    # 签到链接
    REFERER_URL = 'https://webstatic.mihoyo.com/bh3/event/signin-cn/index.html?bbs_presentation_style={}&' \
                  'bbs_game_role_required={}&bbs_auth_required={}&act_id={}&utm_source={}&' \
                  'utm_medium={}&utm_campaign={}'.format('fullscreen', 'bh3_cn', 'true', ACT_ID, 'bbs', 'mys', 'icon')
    AWARD_URL = 'https://api-takumi.mihoyo.com/event/bbs_sign_reward/home?act_id={}'.format(ACT_ID)
    # 角色信息
    ROLE_URL = 'https://api-takumi.mihoyo.com/binding/api/getUserGameRolesByCookie?game_biz={}'.format('bh3_cn')
    # 签到奖励列表
    INFO_URL = 'https://api-takumi.mihoyo.com/common/eutheniav2/index?act_id={}&uid={}&region={}'
    SIGN_URL = 'https://api-takumi.mihoyo.com/common/eutheniav2/sign'
    USER_AGENT = 'Mozilla/5.0 (Linux; Android 7.1.2; RMX1991 Build/NZH54D; wv) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 miHoYoBBS/{}'.format(APP_VERSION)


class ProductionConfig(_Config):
    LOG_LEVEL = logging.INFO


class DevelopmentConfig(_Config):
    LOG_LEVEL = logging.DEBUG


RUN_ENV = os.environ.get('RUN_ENV', 'dev')
if RUN_ENV == 'dev':
    CONFIG = DevelopmentConfig()
else:
    CONFIG = ProductionConfig()

log.basicConfig(level=CONFIG.LOG_LEVEL)

MESSGAE_TEMPLATE = '''
{today:#^28}
[{region_name}] {nickname} ({uid})
今日奖励: {award_name} × {award_cnt}
本月累签: {total_sign_day} 天
签到结果: {status}
{end:#^28}'''

CONFIG.MESSGAE_TEMPLATE = MESSGAE_TEMPLATE
