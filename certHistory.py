import sys, requests, re

class crt: #Class to store Cert details and initialize all with empty string
    cid,Logged_At,Not_Before,Not_After,Common_Name,Matching_Identities = ("",)*6
    Cert_Common_Name,Cert_organizationalUnitName,Cert_organizationName,Cert_countryName = ("",)*4

certCount = 5
if len(sys.argv) == 1: #If no argument given output usage
    print("usage: certHistory [Domain] [Count]")
    exit()
elif len(sys.argv) == 2:
    website = sys.argv[1]
    certCount = 5
else:
    website = sys.argv[1]
    certCount = int(sys.argv[2])

results = []

def getCertDetail(cid): #Get details that obtained by id
    response = requests.get("https://crt.sh/?id="+cid, timeout=25)
    if response.ok == False:
        print("Check your connection or try again later")
        exit()
    for line in response.text.splitlines():
        if "Issuer:" in line:                                   #Focus on line contain issuer:
            line = re.findall('Issuer:.+?Validity', line)[0]    #Get between Issuer and Validity
            line = line.replace("&nbsp;","")                    #Remove unnecessary spaces (&nbsp;)
            line = line.replace("<BR>Validity","")              #Remove last 
            line = line.split('</SPAN><BR>')[1]                 #Remove beginning
            data = line.split('<BR>')                           #All our valuable data between these brackets
            return data
        
response = requests.get("https://crt.sh/?q="+website, timeout=25)
if response.ok == False:
    print("Check your connection or try again later")
    exit()
start = 0
count = 1
info = crt()
for line in response.text.splitlines():         #Loop line by line in html body
    if certCount == 0:          #After specified amount it will exit
        break
    if "Issuer Name" in line:                   #Focus after "Issuer Name" found
        start = 1                               #Enable flag to focus
    if start == 1 and "TD" in line:             #Focus only on lines has TD
        content = re.findall('\>(.*?)\<', line) #Get everything between > and < (remove html tags)
        for c in content:                       #"matching identities" returns more then one value
            if len(c) > 2:                      #also there is 0 length contents
                if count == 1:                  #First time get cid
                    info.cid = c
                    count = 2
                elif count == 2:                #second time get Logget at and so on
                    info.Logged_At = c
                    count = 3
                elif count == 3:
                    info.Not_Before = c
                    count = 4
                elif count == 4:
                    info.Not_After = c
                    count = 5
                elif count == 5:
                    info.Common_Name = c
                    count = 6
                elif count == 6:
                    info.Matching_Identities = c
                    count = 7
                elif count == 7:                
                    if ',' in c:            #if there is a comma mean I reach to issuer name field
                        count = 1           #go to the beginning for next cid
                        data = getCertDetail(info.cid)
                        for d in data:      #get details from ID
                            key,value = d.split('=')
                            if key=="commonName":
                                info.Cert_Common_Name = value
                            elif key=="organizationalUnitName":
                                info.Cert_organizationalUnitName = value
                            elif key=="organizationName":
                                info.Cert_organizationName = value
                            elif key=="countryName":
                                info.Cert_countryName = value
                        results.append(info)
                        certCount -= 1
                        info = crt()
                    else:                   #Matching identities has more than 1 value and its last
                        info.Matching_Identities += " "+c
                        
# I got Data, Next is Print
f = open("Hasan_Bagci.txt", "a")
print('\t'.join(['{0}'.format(k, v) for k,v in vars(results[0]).items()]), file=f) #write to file
print('-'*160, file=f)

print('\t'.join(['{0}'.format(k, v) for k,v in vars(results[0]).items()]))      #write to console
print('-'*160)

for crt in results:
    print('\t'.join(['{1}'.format(k, v) for k,v in vars(crt).items()]))         #write to file
    print('\t'.join(['{1}'.format(k, v) for k,v in vars(crt).items()]), file=f) #write to console
f.close()
