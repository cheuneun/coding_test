def solution(players, callings):
    player_index = {}
    for i,player in enumerate(players):
        player_index[player] = i
        
    for c in callings:
        idx = player_index[c]
        front_idx = players[idx-1]
        
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        player_index[c] = idx - 1
        player_index[front_idx] = idx
        
        
    return players