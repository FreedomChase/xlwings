"""
Required Notice: Copyright (C) Zoomer Analytics GmbH.

xlwings PRO is dual-licensed under one of the following licenses:

* PolyForm Noncommercial License 1.0.0 (for noncommercial use):
  https://polyformproject.org/licenses/noncommercial/1.0.0
* xlwings PRO License (for commercial use):
  https://github.com/xlwings/xlwings/blob/main/LICENSE_PRO.txt

Commercial licenses can be purchased at https://www.xlwings.org
"""

from .embedded_code import dump_embedded_code, runpython_embedded_code
from .module_permissions import verify_execute_permission
from .reports import Markdown, MarkdownStyle
from .utils import LicenseHandler

LicenseHandler.validate_license("pro")
