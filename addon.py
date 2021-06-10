from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://www.entrylevelleft.com/feed.xml"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/ep-logo/pbblog4343324/TELE.png"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/ep-logo/pbblog4343324/TELE.png"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup1)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

if __name__ == '__main__':
    plugin.run()
