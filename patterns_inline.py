#!/usr/bin/env python3
"""
Preprocessing Patterns - 内联版本
适用于 run_preprocessing.py，无外部依赖
"""

import re

# =====================
# 1. IP Law 判定
# =====================
JTITLE_PATTERNS = re.compile(
    r"違反商標法|違反著作權法|商標異議|新型專利舉發|商標評定|新型專利異議|侵害專利權有關財產權爭議等|商標註冊|商標法|發明專利舉發|違反著作權法等|侵害專利權有關財產權爭議|著作權法|發明專利申請|侵害著作權有關財產權爭議等|侵害著作權有關財產權爭議等|聲請單獨宣告沒收（智慧財產案件）|發明專利異議|聲請沒收（智慧財產案件）|聲請單獨宣告沒收扣押物（智慧財產案件）|侵害商標權有關財產權爭議等|商標廢止註冊|違反商標法等|排除侵害專利權等|排除侵害商標權行為等|專科沒收(智慧財產案件)|違反專利法|商標廢止|侵害商標權有關財產權爭議|新型專利申請|著作權法等|新式樣專利舉發|違反營業秘密法等|宣告沒收(智慧財產案件)|有關專利事務|新式樣專利異議|聲請單獨宣告沒收（智慧財產案|宣告沒收（智慧財產案件）|違反商標法附帶民訴|損害賠償（專利權）|專利權損害賠償|商標撤銷|營業秘密損害賠償等|因違反著作權法案附帶民訴|排除侵害專利權|排除侵害著作權行為等|著作權集體管理團體條例|排除侵害商標權行為|新式樣專利申請|設計專利舉發|營業秘密限制閱覽|違反營業秘密法|確認專利權等|商標法等|營業秘密損害賠償等（勞動）|損害賠償（智慧財產權）|專利權授權契約事件|其他智慧財產權事件|聲請宣告沒收(智慧財產案件)|專利權移轉登記|有關著作權事務|專利權其他契約爭議事件|有關商標事務|專利法|營業秘密損害賠償|違反著作權法等罪|著作權授權契約事件|商標權移轉登記|使用專利權權利金|聲請裁定單獨宣告沒收(智慧財產案件)|營業秘密法等|排除侵害商標專用權行為等|侵害著作權有關財產權爭議等|損害賠償（商標專用權）|發明專利申請延長專利權期間|著作權團體集體管理條例|不當行使專利權所生損害賠償爭議事項|排除侵害專利權行為|確認商標權等|營業秘密法|塗銷商標權移轉登記|違反營業秘密法等罪|確認著作權|不當行使專利權所生損害賠償爭議|停止侵害專利權行為等|商標權移轉登記等|損害賠償(專利權)|確認著作權等|排除侵害商標專用權行為|專利年費|專利權權利歸屬等|請求排除侵害專利權等|專利權損害賠償等|專利權移轉登記等|著作權權利歸屬等|營業秘密排除侵害等（勞動）|設計專利申請|商標權其他契約爭議事件|因違反商標法案提起附帶民事訴訟|專利權授權契約事件等|違反營業秘密等|著作權權利歸屬|商標移轉|損害賠償(專利權)|有關專利權事務|單獨宣告沒收(智慧財產案件)|營業秘密排除侵害|有關智慧財產權事務|損害賠償（著作權）|專利權報酬爭議|請求侵害專利權有關財產權爭議|防止侵害專利權行為|商標權授權契約事件等|著作權報酬爭議|請求侵害專利權有關財產權爭議等|商標權權利歸屬|排除侵害（專利權）|確認著作權存在|聲請單獨宣告沒收違禁物（智慧財產案件）|確認著作權授權關係不存在|不當行使智慧財產權爭議事項|排除侵害專利權行為|確認商標權等|營業秘密法|塗銷商標權移轉登記|違反營業秘密法等罪|確認著作權|不當行使智慧財產權爭議事項（勞動）|商標異議等|發明專利申請案主張優先權|侵害專利權有關財產權爭議等|侵害商標權有關財產權爭議等|侵害著作權有關財產權爭議等|侵害商標權有關財產權爭議等聲請再審|侵害專利權有關財產權爭議等聲請訴訟救助|侵害商標權有關財產權爭議等（|侵害著作權有關財產權爭議等（|侵害專利權有關財產權爭議等（|侵害商標權有關財產權爭議等（|侵害著作權有關財產權爭議等（|侵害專利權有關財產權爭議等（|侵害商標權有關財產權爭議等（|侵害著作權有關財產權爭議等（|侵害專利權有關財產權爭議等（|侵害商標權有關財產權爭議等（|侵害著作權有关財產權爭議等（|侵害專利權有關財產權爭議等（|侵害商標權有關財產權爭議等（|侵害著作權有关財產權爭議等（|侵害專利權有關財產權爭議等（|侵害商標權有關財產權爭議等（|侵害著作權有关財產權爭議等（|侵害專利權有關財產權爭議等（|侵害商標權有關財產權爭議等（|侵害著作權有关財產權爭議等（|侵害專利權有關財產權爭議等（|侵害商標權有關財產權爭議等（|侵害著作權有关財產權爭議等（|侵害專利權有關財產權爭議等（|侵害商標權有關財產權爭議等（|侵害著作權有关財產權爭議等（|侵害專利權有關財產權爭議等（|侵害商標權有關財產權爭議等（|侵害著作權有关財產權爭議等（|侵害專利權有關財產權爭議等（|侵害商標權有關財產權爭議等（|侵害著作權有关財產權爭議等（|侵害專利權有關財產權爭議等（|侵害商標權有關財產權爭議等（|侵害著作權有关財產權爭議等（|侵害專利權有關財產權爭議等（|侵害商標權有關財產權爭議等（|侵害著作權有关財產權爭議等|"
)

def is_ip_case(title):
    """根據 JTITLE_PATTERNS 判斷是否為智慧財產權案件"""
    return bool(JTITLE_PATTERNS.search(title))

# =====================
# 2. 案件類型判斷
# =====================
def classify_jtype(title, jcase):
    """
    根據 JCASE 或 JTITLE 判斷案件類型
    返回: CIVIL / CRIMINAL / ADMINISTRATIVE / CWC / RULING / OTHERS
    """
    text = (title or "") + " " + (jcase or "")
    text = text.upper()

    # 優先檢查 CWC (智慧財產案件)
    if "智慧財產" in text or "IPC" in text or "智財" in text:
        return "CWC"

    # 檢查民事
    if re.search(r"民事|民\.?上|支付|確定|公示|審(?:聲|異|撤銷|抗告|理|核定|判)", text):
        return "CIVIL"

    # 檢查刑事
    if re.search(r"刑事|刑上?訴|上?訴|上?审|公訴|聲?請|判決|判", text):
        return "CRIMINAL"

    # 檢查行政
    if re.search(r"行政|訴願|行政訴訟|專利舉發|商標異議|商標評定|撤銷註冊|异議", text):
        return "ADMINISTRATIVE"

    # 檢查裁定/再審等
    if re.search(r"裁定|提審|非常上訴|再審|抗告|更審|發回", text):
        return "RULING"

    return "OTHERS"

# =====================
# 3. 判決結果 VERDICT 分類
# =====================

# 特殊情況優先匹配
Settlement_Success = re.compile(r"(和解成立|撤回訴訟|調解成立|撤回起訴|和解筆錄)")
Settlement_Partial = re.compile(r"部分和解")
Remand = re.compile(r"發回(?:更審|原審)")

# CIVIL 的 WIN/LOSE/PARTIAL
CIVIL_WIN = re.compile(
    r"(?:原告|上訴人|告訴人).{0,30}?(?:勝訴|有理由|應予准許|應給付|准予|許可|照准|應予給付)"
    r"|駁回(?:被告|被上訴人|相對人).{0,30}?之訴"
    r"|(?:被告|被上訴人|相對人)(?:應|應於)?(?:連帶)?.{0,50}?(?:給付|各給付)"
    r"|訴訟費用.{0,50}?由被告(?:連帶|等)?.{0,50}?(?:負擔|平均負擔)"
    r"|(?:應將註冊第.{0,50}?商標.{0,50}?移轉登記予(?:原告|上訴人))"
    r"|(?:確認.{0,50}?為.{0,50}?商標權人)"
    r"|(?:主張成立|契約關係成立)"
)
CIVIL_LOSS = re.compile(r"(?:原告|上訴人).{0,30}?(?:敗訴|無理由|駁回|均無理由|駁回其訴|駁回其請求)")
CIVIL_PARTIAL = re.compile(
    r"(?:部分|一部)(?:勝訴|有理由|應予給付|准許)"
    r"|就.{0,50}?部分(?:勝訴|有理由|准許)"
    r"|駁回(?:部分|一部)(?:之訴|請求)"
    r"|駁回部分"
    r"|被告[應]?連帶(?:負擔|給付).{0,50}?(?:其餘由原告負擔|原告其餘假執行之聲請駁回)"
)

# CRIMINAL 的 WIN/LOSE
CRIMINAL_WIN = re.compile(r"無罪|免刑|免訴|不受理|撤銷|發回更審")
CRIMINAL_LOSS = re.compile(r"有罪|緩刑|拘役|罰金|有期徒刑|無期徒刑")

# ADMINISTRATIVE
ADMIN_WIN = re.compile(r"撤銷|發回|變更|取消|廢止|確認無效|應予許可|應予註冊")
ADMIN_LOSS = re.compile(r"駁回|維持|不予許可|不予註冊|應予駁回")

def classify_verdict(main_clause, j_type, ip_law):
    """
    根據主文、案件類型、是否為IP案件，返回 VERDICT 分類
    可能值: Win, Lose, Mixed, Settlement_Success, Settlement_Partial, Remand, Other
    """
    # 優先檢查特殊情況
    if Settlement_Success.search(main_clause):
        return "Settlement_Success"
    if Settlement_Partial.search(main_clause):
        return "Settlement_Partial"
    if Remand.search(main_clause):
        return "Remand"

    # 非IP或非主要類型回傳 Other
    if j_type in ["RULING", "OTHERS"] or not ip_law:
        return "Other"

    if j_type == "CIVIL":
        if CIVIL_PARTIAL.search(main_clause):
            return "Mixed"
        if CIVIL_WIN.search(main_clause):
            return "Win"
        if CIVIL_LOSS.search(main_clause):
            return "Lose"
        return "Other"

    if j_type == "CRIMINAL":
        if CRIMINAL_WIN.search(main_clause):
            return "Win"
        if CRIMINAL_LOSS.search(main_clause):
            return "Lose"
        return "Other"

    if j_type == "ADMINISTRATIVE":
        if ADMIN_WIN.search(main_clause):
            return "Win"
        if ADMIN_LOSS.search(main_clause):
            return "Lose"
        return "Other"

    if j_type == "CWC":
        # CWC 通常視為民事或行政的一種，沿用 CIVIL 邏輯
        if CIVIL_PARTIAL.search(main_clause):
            return "Mixed"
        if CIVIL_WIN.search(main_clause):
            return "Win"
        if CIVIL_LOSS.search(main_clause):
            return "Lose"
        return "Other"

    return "Other"

# =====================
# 4. 輔助函數
# =====================
def extract_main_clause(jfull):
    """
    從判決書全文提取「主文」段落。
    簡單實現：查找 "主文" 或 "理      由" 前後內容。
    """
    if not jfull:
        return ""
    # 常見模式：主文在「主文」與「理由」之間，或在「主文」與「事實」之間
    patterns = [
        r"主文\s*[:：]?\s*(.+?)(?:理由|事實|及|$)",
        r"主文\s*\n\s*(.+?)(?:\n\s*理\s*由|\n\s*事\s*實|\n\s*及|\n\s*$)",
    ]
    for pat in patterns:
        m = re.search(pat, jfull, re.DOTALL)
        if m:
            return m.group(1).strip()
    # 后备：如果找不到，返回全文前 500 字
    return jfull[:500]
