from django.http.request import HttpHeaders
from django.shortcuts import render

from django.http import HttpResponse
import requests
import json



def send_notification(registration_ids , message_title , message_desc):
    fcm_api = "AAAAtAdOUuo:APA91bE8upJ29nsk3gNuTn-e_ydkEc5E39N4HkEZQWcPTyrGiX5xRuY5JL4iRDn_3H68AI6MPxlwL7HOaBJm3dUzsrjGXfRtfKJUx0TEm6iPiG_ySnkkCRs1BRny3hkR2v806W81Qhj9"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            "image" : "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
            "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())





def index(request):
    return render(request , 'index.html')

def send(request):
    resgistration  = ['cLw2K2cZP8oVGzC7Zm2qV2:APA91bG6Q7ZIYRd8dQjk-taKek7gdCu_Zqf101MQAOBiKPFKsjgwsqYvIAnODYkzS6i2AMDVE7_B2j3XtCy0AeyREkCJLJuZWjalUGi4EEPHdeOnPe5vlvEB4sa7MJeqKamb7o4rAVkB',
    'fPRdkibmAZjNfJWvZLvn49:APA91bGzZyojozZif8tuikK5O4Le73-jWlBhj2Iigfxkl95Nwff6FBhM572QgGGiYcMgA-ffXavCQ0tBXVDXZVoPsFnMN4rwOfmAQcV-0WpAl8pUQHeZ3nFePd8qpDCoRRyXG3WMlyjJ'
    ]
    send_notification(resgistration , 'Code Keen added a new video' , 'Code Keen new video alert')
    return HttpResponse("sent")




def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyA5QXTBDrkkt6RKDiEJlz2xVjq_YAL7Jww",' \
         '        authDomain: "ludo-27977.firebaseapp.com",' \
         '        databaseURL: "https://ludo-27977-default-rtdb.firebaseio.com",' \
         '        projectId: "ludo-27977",' \
         '        storageBucket: "ludo-27977.appspot.com",' \
         '        messagingSenderId: "773216686826",' \
         '        appId: "1:773216686826:web:2c86813e6a5a284914bd93",' \
         '        measurementId: "G-D84371JPYJ"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")