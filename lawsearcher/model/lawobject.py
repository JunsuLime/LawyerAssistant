STATUTE = 0     # 법령
ADMINISTRATIVE_RULE = 1     # 행정규칙
AUTONOMOUS_RULE = 2     # 자치법규
JUDICIAL_PRECEDENT = 3      # 판례
SEPARATE_DECREE = 4       # 별표, 서식
PRESCRIPT = 5       # 규정
ETC_RULE = 6        # 기타


class LawObject(object):
    pass


class Statute(LawObject):
    def __init__(self, name):
        self.name = name
        pass


class JudicialPrecedent(LawObject):
    def __init__(self, code):
        self.code = code
