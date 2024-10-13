async def to_dict(data: str):
    data = data.split('=')[1:]
    data_ = {}
    for i in range(0, len(data), 2):
        data_[data[i]] = data[i + 1]
    return data_


async def check_moves(com: str) -> bool:
    # algorithm dabdala ekanligini bilaman bu endi kirib kelgan vaqtimda yozilgan
    moves_ = [
        {'0', '1', '2'},
        {'3', '4', '5'},
        {'6', '7', '8'},
        {'0', '3', '6'},
        {'1', '4', '7'},
        {'2', '5', '8'},
        {'0', '4', '8'},
        {'2', '4', '6'},
    ]
    return set(com.split('_')) in moves_


async def moves(data) -> str:
    txt = ""
    for i in range(9):
        txt += " ❌ " if data["x"].find(str(i)) != -1 else " ⭕️ " if data["o"].find(
            str(i)) != -1 else " ⬜ "
        if i in (2, 5):
            txt += '\n'
    return txt
