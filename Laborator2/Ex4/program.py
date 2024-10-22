def compose(notes, moves, start_pos):
    # Initialize the result list with the starting note
    song = [notes[start_pos]]

    # Keep track of the current position
    current_pos = start_pos

    for move in moves:
        current_pos = (current_pos + move) % len(notes)

        song.append(notes[current_pos])

    return song

print (compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) )