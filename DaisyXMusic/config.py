 
# MANmusicBOT - Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by exKAMUUU

import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBUa3P0U8HfcilFtPP84n6M4oTPhSWDqiDR2c-kCa4AMt46xk4TcoTi-Tf8-piRcZfF1JiQPXdoM2Q7zzAA5HdD0oVnnODtWdW_Df8irPCDcd4hbVtEWmiZFQLU4gYuNn-G5Mxk2_q8waPDv6B0FIuMJbugq7XD1Jm3T_t7rmwjbPXlX7QV8EcZb1JIJlncUo4toHovq9DU3egqND9vtWVFgnx_i3eBNpYQ2BfNW3yT0plDV892D3nOW8NGdHKO51yv1ehhtY4PWCEGPKF7WdYct8F6KtdpsHY0WqtR91MHKPSNfa_CXOVc-YaWL8viCNK6Pie4RtkZBE_iqgwuqg9EAAAAAUfAUeYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5489665304:AAG0LMcAZVdhOagSoLpDY9yeeG_A8y-cl4Q")
BOT_NAME = getenv("BOT_NAME" "★彡[AƦTEMꞮDE MUSꞮC]彡★")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Artemide001")
BOT_IMG = getenv("BOT_IMG", "https://telegra.ph/file/2b7f803178386c0d428c3.jpg")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID", "21849173"))
API_HASH = getenv("API_HASH", "5d4ae6614b45dc890f3cbe3980c493f3")
BOT_USERNAME = getenv("BOT_USERNAME", "Artemide_Musix_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Artemide_assisant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Artemide001")
PROJECT_NAME = getenv("PROJECT_NAME", "Artemide")
SOURCE_CODE = getenv("SOURCE_CODE", "telegra.ph/PANDUAN-MAN-MUSIC-BOT-07-04")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "-1001687990567")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5498753510").split()))
