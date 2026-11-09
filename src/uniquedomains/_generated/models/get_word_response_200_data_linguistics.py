from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_word_response_200_data_linguistics_memorability_label_type_1 import (
    GetWordResponse200DataLinguisticsMemorabilityLabelType1,
    check_get_word_response_200_data_linguistics_memorability_label_type_1,
)
from ..models.get_word_response_200_data_linguistics_memorability_label_type_2_type_1 import (
    GetWordResponse200DataLinguisticsMemorabilityLabelType2Type1,
    check_get_word_response_200_data_linguistics_memorability_label_type_2_type_1,
)
from ..models.get_word_response_200_data_linguistics_memorability_label_type_3_type_1 import (
    GetWordResponse200DataLinguisticsMemorabilityLabelType3Type1,
    check_get_word_response_200_data_linguistics_memorability_label_type_3_type_1,
)
from ..models.get_word_response_200_data_linguistics_pronounceability_label_type_1 import (
    GetWordResponse200DataLinguisticsPronounceabilityLabelType1,
    check_get_word_response_200_data_linguistics_pronounceability_label_type_1,
)
from ..models.get_word_response_200_data_linguistics_pronounceability_label_type_2_type_1 import (
    GetWordResponse200DataLinguisticsPronounceabilityLabelType2Type1,
    check_get_word_response_200_data_linguistics_pronounceability_label_type_2_type_1,
)
from ..models.get_word_response_200_data_linguistics_pronounceability_label_type_3_type_1 import (
    GetWordResponse200DataLinguisticsPronounceabilityLabelType3Type1,
    check_get_word_response_200_data_linguistics_pronounceability_label_type_3_type_1,
)
from ..models.get_word_response_200_data_linguistics_pronunciation_confidence_type_1 import (
    GetWordResponse200DataLinguisticsPronunciationConfidenceType1,
    check_get_word_response_200_data_linguistics_pronunciation_confidence_type_1,
)
from ..models.get_word_response_200_data_linguistics_pronunciation_confidence_type_2_type_1 import (
    GetWordResponse200DataLinguisticsPronunciationConfidenceType2Type1,
    check_get_word_response_200_data_linguistics_pronunciation_confidence_type_2_type_1,
)
from ..models.get_word_response_200_data_linguistics_pronunciation_confidence_type_3_type_1 import (
    GetWordResponse200DataLinguisticsPronunciationConfidenceType3Type1,
    check_get_word_response_200_data_linguistics_pronunciation_confidence_type_3_type_1,
)
from ..models.get_word_response_200_data_linguistics_sound_texture_label_type_1 import (
    GetWordResponse200DataLinguisticsSoundTextureLabelType1,
    check_get_word_response_200_data_linguistics_sound_texture_label_type_1,
)
from ..models.get_word_response_200_data_linguistics_sound_texture_label_type_2_type_1 import (
    GetWordResponse200DataLinguisticsSoundTextureLabelType2Type1,
    check_get_word_response_200_data_linguistics_sound_texture_label_type_2_type_1,
)
from ..models.get_word_response_200_data_linguistics_sound_texture_label_type_3_type_1 import (
    GetWordResponse200DataLinguisticsSoundTextureLabelType3Type1,
    check_get_word_response_200_data_linguistics_sound_texture_label_type_3_type_1,
)
from ..models.get_word_response_200_data_linguistics_spelling_label_type_1 import (
    GetWordResponse200DataLinguisticsSpellingLabelType1,
    check_get_word_response_200_data_linguistics_spelling_label_type_1,
)
from ..models.get_word_response_200_data_linguistics_spelling_label_type_2_type_1 import (
    GetWordResponse200DataLinguisticsSpellingLabelType2Type1,
    check_get_word_response_200_data_linguistics_spelling_label_type_2_type_1,
)
from ..models.get_word_response_200_data_linguistics_spelling_label_type_3_type_1 import (
    GetWordResponse200DataLinguisticsSpellingLabelType3Type1,
    check_get_word_response_200_data_linguistics_spelling_label_type_3_type_1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWordResponse200DataLinguistics")


@_attrs_define
class GetWordResponse200DataLinguistics:
    """
    Attributes:
        lookalike_is_lookalike (bool | None | Unset):
        lookalike_normalized (None | str | Unset):
        memorability_familiarity (int | None | Unset):
        memorability_label (GetWordResponse200DataLinguisticsMemorabilityLabelType1 |
            GetWordResponse200DataLinguisticsMemorabilityLabelType2Type1 |
            GetWordResponse200DataLinguisticsMemorabilityLabelType3Type1 | None | Unset):
        memorability_neighbors (int | None | Unset):
        memorability_score (int | None | Unset):
        pronounceability_label (GetWordResponse200DataLinguisticsPronounceabilityLabelType1 |
            GetWordResponse200DataLinguisticsPronounceabilityLabelType2Type1 |
            GetWordResponse200DataLinguisticsPronounceabilityLabelType3Type1 | None | Unset):
        pronounceability_phonotactic (int | None | Unset):
        pronounceability_score (int | None | Unset):
        pronunciation_arpabet (None | str | Unset):
        pronunciation_confidence (GetWordResponse200DataLinguisticsPronunciationConfidenceType1 |
            GetWordResponse200DataLinguisticsPronunciationConfidenceType2Type1 |
            GetWordResponse200DataLinguisticsPronunciationConfidenceType3Type1 | None | Unset):
        pronunciation_ipa (None | str | Unset):
        pronunciation_stress_pattern (None | str | Unset):
        pronunciation_syllables (int | None | Unset):
        sound_texture_label (GetWordResponse200DataLinguisticsSoundTextureLabelType1 |
            GetWordResponse200DataLinguisticsSoundTextureLabelType2Type1 |
            GetWordResponse200DataLinguisticsSoundTextureLabelType3Type1 | None | Unset):
        sound_texture_sharpness (int | None | Unset):
        sound_texture_softness (int | None | Unset):
        spelling_homophones (int | None | Unset):
        spelling_label (GetWordResponse200DataLinguisticsSpellingLabelType1 |
            GetWordResponse200DataLinguisticsSpellingLabelType2Type1 |
            GetWordResponse200DataLinguisticsSpellingLabelType3Type1 | None | Unset):
        spelling_likely_misspellings (list[str] | Unset):
        spelling_risk (int | None | Unset):
        spelling_soundalikes (int | None | Unset):
    """

    lookalike_is_lookalike: bool | None | Unset = UNSET
    lookalike_normalized: None | str | Unset = UNSET
    memorability_familiarity: int | None | Unset = UNSET
    memorability_label: (
        GetWordResponse200DataLinguisticsMemorabilityLabelType1
        | GetWordResponse200DataLinguisticsMemorabilityLabelType2Type1
        | GetWordResponse200DataLinguisticsMemorabilityLabelType3Type1
        | None
        | Unset
    ) = UNSET
    memorability_neighbors: int | None | Unset = UNSET
    memorability_score: int | None | Unset = UNSET
    pronounceability_label: (
        GetWordResponse200DataLinguisticsPronounceabilityLabelType1
        | GetWordResponse200DataLinguisticsPronounceabilityLabelType2Type1
        | GetWordResponse200DataLinguisticsPronounceabilityLabelType3Type1
        | None
        | Unset
    ) = UNSET
    pronounceability_phonotactic: int | None | Unset = UNSET
    pronounceability_score: int | None | Unset = UNSET
    pronunciation_arpabet: None | str | Unset = UNSET
    pronunciation_confidence: (
        GetWordResponse200DataLinguisticsPronunciationConfidenceType1
        | GetWordResponse200DataLinguisticsPronunciationConfidenceType2Type1
        | GetWordResponse200DataLinguisticsPronunciationConfidenceType3Type1
        | None
        | Unset
    ) = UNSET
    pronunciation_ipa: None | str | Unset = UNSET
    pronunciation_stress_pattern: None | str | Unset = UNSET
    pronunciation_syllables: int | None | Unset = UNSET
    sound_texture_label: (
        GetWordResponse200DataLinguisticsSoundTextureLabelType1
        | GetWordResponse200DataLinguisticsSoundTextureLabelType2Type1
        | GetWordResponse200DataLinguisticsSoundTextureLabelType3Type1
        | None
        | Unset
    ) = UNSET
    sound_texture_sharpness: int | None | Unset = UNSET
    sound_texture_softness: int | None | Unset = UNSET
    spelling_homophones: int | None | Unset = UNSET
    spelling_label: (
        GetWordResponse200DataLinguisticsSpellingLabelType1
        | GetWordResponse200DataLinguisticsSpellingLabelType2Type1
        | GetWordResponse200DataLinguisticsSpellingLabelType3Type1
        | None
        | Unset
    ) = UNSET
    spelling_likely_misspellings: list[str] | Unset = UNSET
    spelling_risk: int | None | Unset = UNSET
    spelling_soundalikes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lookalike_is_lookalike: bool | None | Unset
        if isinstance(self.lookalike_is_lookalike, Unset):
            lookalike_is_lookalike = UNSET
        else:
            lookalike_is_lookalike = self.lookalike_is_lookalike

        lookalike_normalized: None | str | Unset
        if isinstance(self.lookalike_normalized, Unset):
            lookalike_normalized = UNSET
        else:
            lookalike_normalized = self.lookalike_normalized

        memorability_familiarity: int | None | Unset
        if isinstance(self.memorability_familiarity, Unset):
            memorability_familiarity = UNSET
        else:
            memorability_familiarity = self.memorability_familiarity

        memorability_label: None | str | Unset
        if isinstance(self.memorability_label, Unset):
            memorability_label = UNSET
        elif (
            isinstance(self.memorability_label, str)
            or isinstance(self.memorability_label, str)
            or isinstance(self.memorability_label, str)
        ):
            memorability_label = self.memorability_label
        else:
            memorability_label = self.memorability_label

        memorability_neighbors: int | None | Unset
        if isinstance(self.memorability_neighbors, Unset):
            memorability_neighbors = UNSET
        else:
            memorability_neighbors = self.memorability_neighbors

        memorability_score: int | None | Unset
        if isinstance(self.memorability_score, Unset):
            memorability_score = UNSET
        else:
            memorability_score = self.memorability_score

        pronounceability_label: None | str | Unset
        if isinstance(self.pronounceability_label, Unset):
            pronounceability_label = UNSET
        elif (
            isinstance(self.pronounceability_label, str)
            or isinstance(self.pronounceability_label, str)
            or isinstance(self.pronounceability_label, str)
        ):
            pronounceability_label = self.pronounceability_label
        else:
            pronounceability_label = self.pronounceability_label

        pronounceability_phonotactic: int | None | Unset
        if isinstance(self.pronounceability_phonotactic, Unset):
            pronounceability_phonotactic = UNSET
        else:
            pronounceability_phonotactic = self.pronounceability_phonotactic

        pronounceability_score: int | None | Unset
        if isinstance(self.pronounceability_score, Unset):
            pronounceability_score = UNSET
        else:
            pronounceability_score = self.pronounceability_score

        pronunciation_arpabet: None | str | Unset
        if isinstance(self.pronunciation_arpabet, Unset):
            pronunciation_arpabet = UNSET
        else:
            pronunciation_arpabet = self.pronunciation_arpabet

        pronunciation_confidence: None | str | Unset
        if isinstance(self.pronunciation_confidence, Unset):
            pronunciation_confidence = UNSET
        elif (
            isinstance(self.pronunciation_confidence, str)
            or isinstance(self.pronunciation_confidence, str)
            or isinstance(self.pronunciation_confidence, str)
        ):
            pronunciation_confidence = self.pronunciation_confidence
        else:
            pronunciation_confidence = self.pronunciation_confidence

        pronunciation_ipa: None | str | Unset
        if isinstance(self.pronunciation_ipa, Unset):
            pronunciation_ipa = UNSET
        else:
            pronunciation_ipa = self.pronunciation_ipa

        pronunciation_stress_pattern: None | str | Unset
        if isinstance(self.pronunciation_stress_pattern, Unset):
            pronunciation_stress_pattern = UNSET
        else:
            pronunciation_stress_pattern = self.pronunciation_stress_pattern

        pronunciation_syllables: int | None | Unset
        if isinstance(self.pronunciation_syllables, Unset):
            pronunciation_syllables = UNSET
        else:
            pronunciation_syllables = self.pronunciation_syllables

        sound_texture_label: None | str | Unset
        if isinstance(self.sound_texture_label, Unset):
            sound_texture_label = UNSET
        elif (
            isinstance(self.sound_texture_label, str)
            or isinstance(self.sound_texture_label, str)
            or isinstance(self.sound_texture_label, str)
        ):
            sound_texture_label = self.sound_texture_label
        else:
            sound_texture_label = self.sound_texture_label

        sound_texture_sharpness: int | None | Unset
        if isinstance(self.sound_texture_sharpness, Unset):
            sound_texture_sharpness = UNSET
        else:
            sound_texture_sharpness = self.sound_texture_sharpness

        sound_texture_softness: int | None | Unset
        if isinstance(self.sound_texture_softness, Unset):
            sound_texture_softness = UNSET
        else:
            sound_texture_softness = self.sound_texture_softness

        spelling_homophones: int | None | Unset
        if isinstance(self.spelling_homophones, Unset):
            spelling_homophones = UNSET
        else:
            spelling_homophones = self.spelling_homophones

        spelling_label: None | str | Unset
        if isinstance(self.spelling_label, Unset):
            spelling_label = UNSET
        elif (
            isinstance(self.spelling_label, str)
            or isinstance(self.spelling_label, str)
            or isinstance(self.spelling_label, str)
        ):
            spelling_label = self.spelling_label
        else:
            spelling_label = self.spelling_label

        spelling_likely_misspellings: list[str] | Unset = UNSET
        if not isinstance(self.spelling_likely_misspellings, Unset):
            spelling_likely_misspellings = self.spelling_likely_misspellings

        spelling_risk: int | None | Unset
        if isinstance(self.spelling_risk, Unset):
            spelling_risk = UNSET
        else:
            spelling_risk = self.spelling_risk

        spelling_soundalikes: int | None | Unset
        if isinstance(self.spelling_soundalikes, Unset):
            spelling_soundalikes = UNSET
        else:
            spelling_soundalikes = self.spelling_soundalikes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lookalike_is_lookalike is not UNSET:
            field_dict["lookalikeIsLookalike"] = lookalike_is_lookalike
        if lookalike_normalized is not UNSET:
            field_dict["lookalikeNormalized"] = lookalike_normalized
        if memorability_familiarity is not UNSET:
            field_dict["memorabilityFamiliarity"] = memorability_familiarity
        if memorability_label is not UNSET:
            field_dict["memorabilityLabel"] = memorability_label
        if memorability_neighbors is not UNSET:
            field_dict["memorabilityNeighbors"] = memorability_neighbors
        if memorability_score is not UNSET:
            field_dict["memorabilityScore"] = memorability_score
        if pronounceability_label is not UNSET:
            field_dict["pronounceabilityLabel"] = pronounceability_label
        if pronounceability_phonotactic is not UNSET:
            field_dict["pronounceabilityPhonotactic"] = pronounceability_phonotactic
        if pronounceability_score is not UNSET:
            field_dict["pronounceabilityScore"] = pronounceability_score
        if pronunciation_arpabet is not UNSET:
            field_dict["pronunciationArpabet"] = pronunciation_arpabet
        if pronunciation_confidence is not UNSET:
            field_dict["pronunciationConfidence"] = pronunciation_confidence
        if pronunciation_ipa is not UNSET:
            field_dict["pronunciationIpa"] = pronunciation_ipa
        if pronunciation_stress_pattern is not UNSET:
            field_dict["pronunciationStressPattern"] = pronunciation_stress_pattern
        if pronunciation_syllables is not UNSET:
            field_dict["pronunciationSyllables"] = pronunciation_syllables
        if sound_texture_label is not UNSET:
            field_dict["soundTextureLabel"] = sound_texture_label
        if sound_texture_sharpness is not UNSET:
            field_dict["soundTextureSharpness"] = sound_texture_sharpness
        if sound_texture_softness is not UNSET:
            field_dict["soundTextureSoftness"] = sound_texture_softness
        if spelling_homophones is not UNSET:
            field_dict["spellingHomophones"] = spelling_homophones
        if spelling_label is not UNSET:
            field_dict["spellingLabel"] = spelling_label
        if spelling_likely_misspellings is not UNSET:
            field_dict["spellingLikelyMisspellings"] = spelling_likely_misspellings
        if spelling_risk is not UNSET:
            field_dict["spellingRisk"] = spelling_risk
        if spelling_soundalikes is not UNSET:
            field_dict["spellingSoundalikes"] = spelling_soundalikes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_lookalike_is_lookalike(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        lookalike_is_lookalike = _parse_lookalike_is_lookalike(
            d.pop("lookalikeIsLookalike", UNSET)
        )

        def _parse_lookalike_normalized(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lookalike_normalized = _parse_lookalike_normalized(
            d.pop("lookalikeNormalized", UNSET)
        )

        def _parse_memorability_familiarity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memorability_familiarity = _parse_memorability_familiarity(
            d.pop("memorabilityFamiliarity", UNSET)
        )

        def _parse_memorability_label(
            data: object,
        ) -> (
            GetWordResponse200DataLinguisticsMemorabilityLabelType1
            | GetWordResponse200DataLinguisticsMemorabilityLabelType2Type1
            | GetWordResponse200DataLinguisticsMemorabilityLabelType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                memorability_label_type_1 = check_get_word_response_200_data_linguistics_memorability_label_type_1(
                    data
                )

                return memorability_label_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                memorability_label_type_2_type_1 = check_get_word_response_200_data_linguistics_memorability_label_type_2_type_1(
                    data
                )

                return memorability_label_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                memorability_label_type_3_type_1 = check_get_word_response_200_data_linguistics_memorability_label_type_3_type_1(
                    data
                )

                return memorability_label_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetWordResponse200DataLinguisticsMemorabilityLabelType1
                | GetWordResponse200DataLinguisticsMemorabilityLabelType2Type1
                | GetWordResponse200DataLinguisticsMemorabilityLabelType3Type1
                | None
                | Unset,
                data,
            )

        memorability_label = _parse_memorability_label(
            d.pop("memorabilityLabel", UNSET)
        )

        def _parse_memorability_neighbors(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memorability_neighbors = _parse_memorability_neighbors(
            d.pop("memorabilityNeighbors", UNSET)
        )

        def _parse_memorability_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memorability_score = _parse_memorability_score(
            d.pop("memorabilityScore", UNSET)
        )

        def _parse_pronounceability_label(
            data: object,
        ) -> (
            GetWordResponse200DataLinguisticsPronounceabilityLabelType1
            | GetWordResponse200DataLinguisticsPronounceabilityLabelType2Type1
            | GetWordResponse200DataLinguisticsPronounceabilityLabelType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pronounceability_label_type_1 = check_get_word_response_200_data_linguistics_pronounceability_label_type_1(
                    data
                )

                return pronounceability_label_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pronounceability_label_type_2_type_1 = check_get_word_response_200_data_linguistics_pronounceability_label_type_2_type_1(
                    data
                )

                return pronounceability_label_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pronounceability_label_type_3_type_1 = check_get_word_response_200_data_linguistics_pronounceability_label_type_3_type_1(
                    data
                )

                return pronounceability_label_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetWordResponse200DataLinguisticsPronounceabilityLabelType1
                | GetWordResponse200DataLinguisticsPronounceabilityLabelType2Type1
                | GetWordResponse200DataLinguisticsPronounceabilityLabelType3Type1
                | None
                | Unset,
                data,
            )

        pronounceability_label = _parse_pronounceability_label(
            d.pop("pronounceabilityLabel", UNSET)
        )

        def _parse_pronounceability_phonotactic(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pronounceability_phonotactic = _parse_pronounceability_phonotactic(
            d.pop("pronounceabilityPhonotactic", UNSET)
        )

        def _parse_pronounceability_score(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pronounceability_score = _parse_pronounceability_score(
            d.pop("pronounceabilityScore", UNSET)
        )

        def _parse_pronunciation_arpabet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pronunciation_arpabet = _parse_pronunciation_arpabet(
            d.pop("pronunciationArpabet", UNSET)
        )

        def _parse_pronunciation_confidence(
            data: object,
        ) -> (
            GetWordResponse200DataLinguisticsPronunciationConfidenceType1
            | GetWordResponse200DataLinguisticsPronunciationConfidenceType2Type1
            | GetWordResponse200DataLinguisticsPronunciationConfidenceType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pronunciation_confidence_type_1 = check_get_word_response_200_data_linguistics_pronunciation_confidence_type_1(
                    data
                )

                return pronunciation_confidence_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pronunciation_confidence_type_2_type_1 = check_get_word_response_200_data_linguistics_pronunciation_confidence_type_2_type_1(
                    data
                )

                return pronunciation_confidence_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pronunciation_confidence_type_3_type_1 = check_get_word_response_200_data_linguistics_pronunciation_confidence_type_3_type_1(
                    data
                )

                return pronunciation_confidence_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetWordResponse200DataLinguisticsPronunciationConfidenceType1
                | GetWordResponse200DataLinguisticsPronunciationConfidenceType2Type1
                | GetWordResponse200DataLinguisticsPronunciationConfidenceType3Type1
                | None
                | Unset,
                data,
            )

        pronunciation_confidence = _parse_pronunciation_confidence(
            d.pop("pronunciationConfidence", UNSET)
        )

        def _parse_pronunciation_ipa(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pronunciation_ipa = _parse_pronunciation_ipa(d.pop("pronunciationIpa", UNSET))

        def _parse_pronunciation_stress_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pronunciation_stress_pattern = _parse_pronunciation_stress_pattern(
            d.pop("pronunciationStressPattern", UNSET)
        )

        def _parse_pronunciation_syllables(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pronunciation_syllables = _parse_pronunciation_syllables(
            d.pop("pronunciationSyllables", UNSET)
        )

        def _parse_sound_texture_label(
            data: object,
        ) -> (
            GetWordResponse200DataLinguisticsSoundTextureLabelType1
            | GetWordResponse200DataLinguisticsSoundTextureLabelType2Type1
            | GetWordResponse200DataLinguisticsSoundTextureLabelType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sound_texture_label_type_1 = check_get_word_response_200_data_linguistics_sound_texture_label_type_1(
                    data
                )

                return sound_texture_label_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sound_texture_label_type_2_type_1 = check_get_word_response_200_data_linguistics_sound_texture_label_type_2_type_1(
                    data
                )

                return sound_texture_label_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sound_texture_label_type_3_type_1 = check_get_word_response_200_data_linguistics_sound_texture_label_type_3_type_1(
                    data
                )

                return sound_texture_label_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetWordResponse200DataLinguisticsSoundTextureLabelType1
                | GetWordResponse200DataLinguisticsSoundTextureLabelType2Type1
                | GetWordResponse200DataLinguisticsSoundTextureLabelType3Type1
                | None
                | Unset,
                data,
            )

        sound_texture_label = _parse_sound_texture_label(
            d.pop("soundTextureLabel", UNSET)
        )

        def _parse_sound_texture_sharpness(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sound_texture_sharpness = _parse_sound_texture_sharpness(
            d.pop("soundTextureSharpness", UNSET)
        )

        def _parse_sound_texture_softness(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sound_texture_softness = _parse_sound_texture_softness(
            d.pop("soundTextureSoftness", UNSET)
        )

        def _parse_spelling_homophones(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        spelling_homophones = _parse_spelling_homophones(
            d.pop("spellingHomophones", UNSET)
        )

        def _parse_spelling_label(
            data: object,
        ) -> (
            GetWordResponse200DataLinguisticsSpellingLabelType1
            | GetWordResponse200DataLinguisticsSpellingLabelType2Type1
            | GetWordResponse200DataLinguisticsSpellingLabelType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                spelling_label_type_1 = (
                    check_get_word_response_200_data_linguistics_spelling_label_type_1(
                        data
                    )
                )

                return spelling_label_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                spelling_label_type_2_type_1 = check_get_word_response_200_data_linguistics_spelling_label_type_2_type_1(
                    data
                )

                return spelling_label_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                spelling_label_type_3_type_1 = check_get_word_response_200_data_linguistics_spelling_label_type_3_type_1(
                    data
                )

                return spelling_label_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GetWordResponse200DataLinguisticsSpellingLabelType1
                | GetWordResponse200DataLinguisticsSpellingLabelType2Type1
                | GetWordResponse200DataLinguisticsSpellingLabelType3Type1
                | None
                | Unset,
                data,
            )

        spelling_label = _parse_spelling_label(d.pop("spellingLabel", UNSET))

        spelling_likely_misspellings = cast(
            list[str], d.pop("spellingLikelyMisspellings", UNSET)
        )

        def _parse_spelling_risk(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        spelling_risk = _parse_spelling_risk(d.pop("spellingRisk", UNSET))

        def _parse_spelling_soundalikes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        spelling_soundalikes = _parse_spelling_soundalikes(
            d.pop("spellingSoundalikes", UNSET)
        )

        get_word_response_200_data_linguistics = cls(
            lookalike_is_lookalike=lookalike_is_lookalike,
            lookalike_normalized=lookalike_normalized,
            memorability_familiarity=memorability_familiarity,
            memorability_label=memorability_label,
            memorability_neighbors=memorability_neighbors,
            memorability_score=memorability_score,
            pronounceability_label=pronounceability_label,
            pronounceability_phonotactic=pronounceability_phonotactic,
            pronounceability_score=pronounceability_score,
            pronunciation_arpabet=pronunciation_arpabet,
            pronunciation_confidence=pronunciation_confidence,
            pronunciation_ipa=pronunciation_ipa,
            pronunciation_stress_pattern=pronunciation_stress_pattern,
            pronunciation_syllables=pronunciation_syllables,
            sound_texture_label=sound_texture_label,
            sound_texture_sharpness=sound_texture_sharpness,
            sound_texture_softness=sound_texture_softness,
            spelling_homophones=spelling_homophones,
            spelling_label=spelling_label,
            spelling_likely_misspellings=spelling_likely_misspellings,
            spelling_risk=spelling_risk,
            spelling_soundalikes=spelling_soundalikes,
        )

        get_word_response_200_data_linguistics.additional_properties = d
        return get_word_response_200_data_linguistics

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
