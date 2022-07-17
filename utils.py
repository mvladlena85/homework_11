import json


def load_candidates_from_json() -> list[dict]:
    # – возвращает список всех кандидатов
    with open('candidates.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_candidate(candidate_id: int) -> dict:
    # возвращает одного кандидата по его id
    candidate_list = load_candidates_from_json()
    for candidate in candidate_list:
        if candidate['id'] == candidate_id:
            return candidate
    return None


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    # возвращает кандидатов по имени
    candidate_list = load_candidates_from_json()
    search_results = []
    for candidate in candidate_list:
        if candidate_name.lower() in candidate['name'].lower():
            search_results.append(candidate)
    return search_results


def get_candidates_by_skill(skill_name):
    # возвращает кандидатов по навыку
    candidate_list = load_candidates_from_json()
    search_results = []
    for candidate in candidate_list:
        skill_list = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skill_list:
            search_results.append(candidate)
    return search_results


# print(load_candidates_from_json())
# print(get_candidate(4))
# print(get_candidates_by_name('she'))
# print(get_candidates_by_skill('python'))
