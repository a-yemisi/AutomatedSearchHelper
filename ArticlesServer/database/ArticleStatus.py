from enum import IntEnum


class ArticleStatus(IntEnum):
    READ_CORRECT_WITH_FINDINGS = 1,
    READ_PARTIAL_WITH_FINDINGS = 2,
    READ_PARTIAL_ERROR_READING_NO_FINDINGS = 3,
    READ_PARTIAL_PUBLISHER_NOT_SUPPORTED_NO_FINDINGS = 4,
    NO_ACCESS_TO_ARTICLE = 5,
    READ_FROM_PDF_NO_FINDINGS = 6,
    READ_CORRECT_NO_FINDINGS = 7,
    ARTICLE_IGNORED = 8,
    ACCEPTED = 9,
    DECLINED = 10,
    PENDING = 11,
    TO_BE_CHECKED = 12

