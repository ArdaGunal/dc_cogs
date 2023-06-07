# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import json
from pathlib import Path

from redbot.core.bot import Red

from .bumphatırlat import BumpReminder

with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]

async def setup(bot:Red) -> None:
  await bot.add_cog(BumpReminder(bot))






