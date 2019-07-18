import AIAssistantFunctions as jf

if __name__ == '__main__':

    jf.wishMe()
    while(True):

        query = jf.takeCommand().lower()

        if 'wikipedia' in query:
            jf.searchWikipedia(query)

        elif 'open youtube' in query:
            jf.searchWeb("youtube")

        elif 'open google' in query:
            jf.searchWeb("google")

        elif 'open stackoverflow' in query:
            jf.searchWeb("stackoverflow")

        elif 'play music' in query:
            jf.playMusic()

        elif 'time' in query:
            jf.getTime()

        elif 'open code' in query:
            jf.openCode()

        elif 'news today'in query:
            jf.news()

        elif 'send email' in query:
           jf.email()

        elif 'quit application' in query:
            jf.quitJarvis()

