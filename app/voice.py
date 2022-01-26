from utils import *


if __name__=='__main__':
    clear = lambda: os.system('cls')
    clear()
    respond("Hi, I'm Sam.")
          
    while(1):
        respond("How can I help you?")
        content=talk().lower()
        
        if content==0:
            continue
            
        if "stop" in str(content) or "exit" in str(content) or "bye" in str(content):
            respond("Ok bye and take care")
            break
            
        if 'wikipedia' in content:
            respond('Searching Wikipedia')
            content =content.replace("wikipedia", "")
            results = wikipedia.summary(content, sentences=3)
            respond("According to Wikipedia")
            print(results)
            respond(results)
                  
        elif 'time' in content:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")     
        
        elif 'search'  in content:
            content = content.replace("search", "")
            webbrowser.open_new_tab(content)
            time.sleep(5)
        
        # elif "calculate" or "what is" in content: 
        #     question=talk()
        #     app_id="API key"
        #     client = wolframalpha.Client(app_id)
        #     res = client.content(question)
        #     answer = next(res.results).content
        #     respond("The answer is " + answer)
            
        elif 'open google' in content:
            webbrowser.open_new_tab("https://www.google.com")
            respond("Google is open")
            time.sleep(5)
            
        elif 'youtube' in content: 
            driver = webdriver.Chrome(r"Mention your webdriver location") 
            driver.implicitly_wait(1) 
            driver.maximize_window()
            respond("Opening in youtube") 
            indx = content.split().index('youtube') 
            content = content.split()[indx + 1:] 
            driver.get("http://www.youtube.com/results?search_content =" + '+'.join(content))              
                
        elif "open word" in content: 
            respond("Opening Microsoft Word") 
            os.startfile('Mention location of Word in your system')

        elif 'open gmail' in content:
            webbrowser.open_new_tab("https://www.gmail.com")
            respond("Gmail is open")
            time.sleep(5)

        # elif 'play music' in content or 'play a song' in content :
        #     respond("Here's your music. Enjoy !")
        #     playMusic() fix mixer issue
        
        elif 'send a mail' or 'send email' in content:
            try:
                if content:
                    respond("What should I say?")
                    content_mail=talk()
                    respond("Whom should i send it to? (Type address)")
                    to = input()   
                    sendEmail(to, content_mail)
                    respond("Email has been sent !")
            except Exception as e:
                print(e)
                respond("I am not able to send this email")
                
        elif 'find file' in content:
            respond('What is the name of the file that I should find ?')
            content = talk()
            filename = content
            print(filename)
            respond('What would be the extension of the file ?')
            content = talk()
            content = content.lower()
            extension = content
            print(extension)
            fullname = str(filename) + '.' + str(extension)
            print(fullname)
            path = r'D:\\'
            location = find(fullname,path)
            respond('File is found at the below location')
            print(location)
            
        elif 'joke' in content:
            respond(pyjokes.get_joke()) 

        elif "battery" in content:
            battery_percent_response =   battery_percent()
            print('Your battery percentage is'+ battery_percent_response)
            respond('Your battery percentage is'+ battery_percent_response)
                
        elif "network" in content:
            print(network_info())
            respond('Network information has been printed to screen...' )
                
        elif "memory" in content:
            memory_info_response = memory_info()
            print('Your memory information is as follows: Total Space is '+ memory_info_response[0]
            + "Used memory space is" + memory_info_response[1]
            + "Available memory space is" + memory_info_response[2]
            + "Percentage memory space is" + memory_info_response[3])     

        elif "process" in content:
            print(process_info())

        # elif "shut down" in content:
        #     respond("Ok , your system will shut down in 10 secs")
        #     subprocess.call(["shutdown", "/l"])  

        else:
           respond("Application not available")