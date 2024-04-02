import math
import heapq

with open("input.txt", "r") as reader:
    num_of_parties = int(reader.readline().strip())
    parties = []
    chosen_active_parties = []
    chosen_active_parties_set = set()
    for i in range(num_of_parties):
        voters, bribe = map(int, reader.readline().strip().split(" "))
        parties.append((voters, i, bribe))
        if bribe != -1 and (voters, bribe) not in chosen_active_parties_set:
            chosen_active_parties.append((voters, i, bribe))
            chosen_active_parties_set.add((voters, bribe))


def play_strategy(parties, chosen_active_parties):
    min_cost = math.inf
    best_party = None
    best_party_voters = None
    rest_votes = []

    for chosen_party in chosen_active_parties:
        pq = [(-votes, index) for votes, index, bribe in parties if index != chosen_party[1]]
        heapq.heapify(pq)
        chosen_party_voters, chosen_party_index, chosen_party_bribe = chosen_party
        current_cost = chosen_party_bribe

        if chosen_party_bribe == -1:
            continue

        # цикл агитации
        while True:
            if chosen_party_voters > (-pq[0][0]):
                # Если выбранная партия стала лидером
                if min_cost > current_cost:
                    min_cost = current_cost
                    best_party = chosen_party_index
                    best_party_voters = chosen_party_voters
                    rest_votes = []
                    for votes, index in pq:
                        # print('final votes here', votes, index)
                        if index == chosen_party_index:
                            continue
                        rest_votes.append((-votes, index))
                break

            # Извлекаем партию-лидера
            leader_votes, leader_index = heapq.heappop(pq)
            leader_votes = -leader_votes

            # Перераспределяем  голоса
            chosen_party_voters += 1
            leader_votes -= 1
            current_cost += 1

            # Обновляем очередь с приоритетами
            heapq.heappush(pq, (-leader_votes, leader_index))

    return min_cost, best_party + 1, best_party_voters, rest_votes


if __name__ == "__main__":
    chosen_active_parties.sort(key=lambda x: x[2])

    if num_of_parties != 1:
        total_cost, best_party_index, best_party_voters, final_votes = play_strategy(parties, chosen_active_parties)
        final_votes_lst = [None] * num_of_parties

        for votes, index in final_votes:
            final_votes_lst[index] = votes
        else:
            final_votes_lst[best_party_index - 1] = best_party_voters
    else:
        total_cost = parties[0][2]
        best_party_index = 1
        final_votes_lst = [parties[0][0]]

with open("output.txt", "w") as file:
    file.write(str(total_cost) + "\n")
    file.write(str(best_party_index) + "\n")
    file.write(" ".join(str(votes) for votes in final_votes_lst))
