from log import log
from measure_process import classify_bought_item


def get_coordinate_from_texts(boxes, texts):
    log("Getting item coordinates")
    buy_list = []

    for i in range(len(boxes['level'])):
        box_text = boxes['text'][i]
        if box_text in texts:
            classify_bought_item(box_text)
            buy_list.append([boxes['left'][i], boxes['top'][i]])

    if len(buy_list) == 0:
        return 0, 0

    return buy_list
