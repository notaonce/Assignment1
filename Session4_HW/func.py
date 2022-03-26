def extract(info_list):
    result = []

    for info in info_list:
        title = info.find("dt").find("a").text
        author = info.find("dd", {"class":"desc"}).find("a").text
        rating = info.find("strong").text

        info_dic = {
            "title" : title ,
            "author" : author ,
            "rating" : rating 
        }

        result.append(info_dic)

    return result
