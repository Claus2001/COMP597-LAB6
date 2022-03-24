import requests
from sys import argv

def main():
    
    user_num = argv[1]
    user_info = get_user_info(user_num)
    if user_info:
        pastebin_string = get_pastebin_string(user_info)
        pasteBin_url = post_to_pastebin(pastebin_string[0], pastebin_string[1])
        print(pasteBin_url)

def post_to_pastebin(tittle, body_text):
#3) Create a function that creates a PasteBin paste having a specified title and body text
    print("Posting to pastebin", end="")

    pasteBin_params = {
        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': tittle
    }

    response = requests.post('https://pastebin.com/api/api_post.php', data=pasteBin_params)

    if response.status_code == 200:
        print("Success")
        return  response.text
    else:
        print('Failed. Response code:',response.status_code)
        return

def get_pastebin_string(user_dict):
    #2) Create a function that builds the strings to be used for the title and body text of a PasteBin 
    #paste.
    tittle = user_dict['forms']['name'], + "'s Abilities"
    body_text = "Name: " +  user_dict['forms']['name'], "\n"
    body_text += "Abilities:" + user_dict['abilities']['ability']['name']
    return (tittle, body_text)

def get_user_info(user_num):
    #1) Create a function that retrieves information for a specified Pokémon from the PokeApi
    print("Getting (pokemon) information...", end="")
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(user_num))

    if response.status_code == 200:
        print("Success")
        return  response.json()
    else:
        print('Failed. Response code:',response.status_code)
        return
main()
