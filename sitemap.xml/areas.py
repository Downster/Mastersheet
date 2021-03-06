import xml.etree.ElementTree as ET
from xml.dom import minidom

areas= [
      {
        "id": "627a1d4b16742255657e800f",
        "uuid": "a6e462e0-3c37-5660-a80a-91fb088a1f2d",
        "areaName": "Sam's Throne & Surroundings",
        "pathTokens": [
          "US",
          "Arkansas",
          "North-Central Arkansas",
          "Sam's Throne & Surroundings"
        ],
        "totalClimbs": 410,
        "density": 68.19949299915771
      },
      {
        "id": "627a1d4b16742255657e8015",
        "uuid": "d0c61f42-b601-568f-a349-4b386c5dd0b0",
        "areaName": "Horseshoe Canyon Ranch",
        "pathTokens": [
          "US",
          "Arkansas",
          "North-Central Arkansas",
          "Horseshoe Canyon Ranch"
        ],
        "totalClimbs": 651,
        "density": 130.2
      },
      {
        "id": "627a1d4c16742255657e84a7",
        "uuid": "47053277-7738-5e02-b3b0-a0fc26a64b07",
        "areaName": "Canon City",
        "pathTokens": [
          "US",
          "Colorado",
          "Canon City"
        ],
        "totalClimbs": 1347,
        "density": 2.596487100187197
      },
      {
        "id": "627a1d4c16742255657e84ab",
        "uuid": "decc1251-4a67-52b9-b23f-3243e10e93d0",
        "areaName": "Boulder",
        "pathTokens": [
          "US",
          "Colorado",
          "Boulder"
        ],
        "totalClimbs": 5140,
        "density": 18.320571273398045
      },
      {
        "id": "627a1d4d16742255657ea860",
        "uuid": "6d8bdd9e-c624-5964-8393-4f6f5fe53d70",
        "areaName": "Mammoth Lakes Area",
        "pathTokens": [
          "US",
          "California",
          "Sierra Eastside",
          "Mammoth Lakes Area"
        ],
        "totalClimbs": 1471,
        "density": 0.7524854494475871
      },
      {
        "id": "627a1d4c16742255657e8520",
        "uuid": "a4aef32e-321a-5c31-896b-88992dc2273d",
        "areaName": "Castlewood Canyon SP",
        "pathTokens": [
          "US",
          "Colorado",
          "Denver Metropolitan Area Bouldering and Buildering",
          "Denver South",
          "Castlewood Canyon SP"
        ],
        "totalClimbs": 545,
        "density": 34.50166686012233
      },
      {
        "id": "627a1d4c16742255657e9f52",
        "uuid": "64ea28d2-8296-5a93-bc4c-cb0a481acf98",
        "areaName": "South Mountain",
        "pathTokens": [
          "US",
          "Arizona",
          "Central Arizona",
          "**Phoenix Areas",
          "South Mountain"
        ],
        "totalClimbs": 450,
        "density": 17.247565540028937
      },
      {
        "id": "627a1d4d16742255657ea997",
        "uuid": "95d927bb-d322-5477-8302-0f3059a7825c",
        "areaName": "Lone Pine Area",
        "pathTokens": [
          "US",
          "California",
          "Sierra Eastside",
          "Lone Pine Area"
        ],
        "totalClimbs": 533,
        "density": 2.1504041430489016
      },
      {
        "id": "627a1d4c16742255657e866e",
        "uuid": "1621a45a-659f-5708-9ba0-bc0a295bfc73",
        "areaName": "RMNP - Rock",
        "pathTokens": [
          "US",
          "Colorado",
          "Alpine Rock",
          "RMNP - Rock"
        ],
        "totalClimbs": 523,
        "density": 0.8675348772030241
      },
      {
        "id": "627a1d4d16742255657eaa2b",
        "uuid": "ed25ebdd-13ac-501e-9b4f-eb02356d9035",
        "areaName": "Santa Barbara",
        "pathTokens": [
          "US",
          "California",
          "Central Coast",
          "Santa Barbara"
        ],
        "totalClimbs": 788,
        "density": 1.8597960932410218
      },
      {
        "id": "627a1d4c16742255657ea044",
        "uuid": "1fdb38a6-6b41-5d20-993c-dcf46fcf25a3",
        "areaName": "Flagstaff Area",
        "pathTokens": [
          "US",
          "Arizona",
          "Northern Arizona",
          "Flagstaff Area"
        ],
        "totalClimbs": 690,
        "density": 1.291072103858679
      },
      {
        "id": "627a1d4c16742255657ea050",
        "uuid": "19dfb197-abbe-5b60-abc0-83f875a4e73b",
        "areaName": "Sedona Area",
        "pathTokens": [
          "US",
          "Arizona",
          "Northern Arizona",
          "Sedona Area"
        ],
        "totalClimbs": 525,
        "density": 2.3264933959556386
      },
      {
        "id": "627a1d4d16742255657eaa62",
        "uuid": "e3feb035-7436-571c-9bcf-d3307c407a66",
        "areaName": "* Mammoth Lakes Bouldering",
        "pathTokens": [
          "US",
          "California",
          "Sierra Eastside",
          "Mammoth Lakes Area",
          "* Mammoth Lakes Bouldering"
        ],
        "totalClimbs": 401,
        "density": 0.5882572398149079
      },
      {
        "id": "627a1d4d16742255657eaa77",
        "uuid": "a6b1ce37-194d-5d3a-9e7a-04151d2c7508",
        "areaName": "Alabama Hills",
        "pathTokens": [
          "US",
          "California",
          "Sierra Eastside",
          "Lone Pine Area",
          "Alabama Hills"
        ],
        "totalClimbs": 430,
        "density": 23.390662524475953
      },
      {
        "id": "627a1d4c16742255657e8787",
        "uuid": "7fea44a6-af9d-583e-9abc-274876289cd7",
        "areaName": "Eldorado Canyon State Park",
        "pathTokens": [
          "US",
          "Colorado",
          "Boulder",
          "Eldorado Canyon State Park"
        ],
        "totalClimbs": 1219,
        "density": 28.607160591850405
      },
      {
        "id": "627a1d4c16742255657e878b",
        "uuid": "e519a674-a620-509c-9e86-a246f84a8e40",
        "areaName": "Boulder Canyon",
        "pathTokens": [
          "US",
          "Colorado",
          "Boulder",
          "Boulder Canyon"
        ],
        "totalClimbs": 1786,
        "density": 26.418318151734397
      },
      {
        "id": "627a1d4c16742255657e8796",
        "uuid": "d0ca78b6-a3cb-517c-adee-d9c6f8c2d2d8",
        "areaName": "Flatirons",
        "pathTokens": [
          "US",
          "Colorado",
          "Boulder",
          "Flatirons"
        ],
        "totalClimbs": 1300,
        "density": 59.4683401887155
      },
      {
        "id": "627a1d4c16742255657e8797",
        "uuid": "ee2fde9f-b2c2-58e8-ad07-ff56ccf69c8a",
        "areaName": "South",
        "pathTokens": [
          "US",
          "Colorado",
          "Boulder",
          "Flatirons",
          "South"
        ],
        "totalClimbs": 425,
        "density": 46.721965717960884
      },
      {
        "id": "627a1d4d16742255657eabd6",
        "uuid": "ee2401d2-45ce-57c1-8c4c-59350d8177d1",
        "areaName": "San Bernardino Mountains",
        "pathTokens": [
          "US",
          "California",
          "San Bernardino Mountains"
        ],
        "totalClimbs": 1912,
        "density": 0.7519256927609603
      },
      {
        "id": "627a1d4d16742255657eabd7",
        "uuid": "6e4088c3-20f4-5e36-a319-c539b3b72275",
        "areaName": "Big Bear Lake Area",
        "pathTokens": [
          "US",
          "California",
          "San Bernardino Mountains",
          "Big Bear Lake Area"
        ],
        "totalClimbs": 958,
        "density": 4.498931581456449
      },
      {
        "id": "627a1d4c16742255657ea298",
        "uuid": "f2591e24-8f94-5cb3-9f02-92bfe3f5cd61",
        "areaName": "Mount Lemmon (Santa Catalina Mountains)",
        "pathTokens": [
          "US",
          "Arizona",
          "Southern Arizona",
          "Mount Lemmon (Santa Catalina Mountains)"
        ],
        "totalClimbs": 2726,
        "density": 3.228597483915047
      },
      {
        "id": "627a1d4c16742255657ea2bf",
        "uuid": "74a365ae-142f-5b24-8198-2ac56dfd2922",
        "areaName": "Mount Lemmon (Catalina Highway)",
        "pathTokens": [
          "US",
          "Arizona",
          "Southern Arizona",
          "Mount Lemmon (Santa Catalina Mountains)",
          "Mount Lemmon (Catalina Highway)"
        ],
        "totalClimbs": 2586,
        "density": 4.391166341980658
      },
      {
        "id": "627a1d4c16742255657ea2c0",
        "uuid": "c9effcac-853e-514e-9cc0-958488e28cf0",
        "areaName": "7 - Upper Highway",
        "pathTokens": [
          "US",
          "Arizona",
          "Southern Arizona",
          "Mount Lemmon (Santa Catalina Mountains)",
          "Mount Lemmon (Catalina Highway)",
          "7 - Upper Highway"
        ],
        "totalClimbs": 492,
        "density": 13.543394629107006
      },
      {
        "id": "627a1d4c16742255657ea2c2",
        "uuid": "ef84cfb7-f347-5d0c-8060-3c5a5b56137b",
        "areaName": "6 - Mid-Mountain",
        "pathTokens": [
          "US",
          "Arizona",
          "Southern Arizona",
          "Mount Lemmon (Santa Catalina Mountains)",
          "Mount Lemmon (Catalina Highway)",
          "6 - Mid-Mountain"
        ],
        "totalClimbs": 420,
        "density": 28.318044571648223
      },
      {
        "id": "627a1d4c16742255657e897f",
        "uuid": "86410ac6-a2da-5a5f-8855-ba74384faafb",
        "areaName": "North",
        "pathTokens": [
          "US",
          "Colorado",
          "Boulder",
          "Flatirons",
          "North"
        ],
        "totalClimbs": 571,
        "density": 114.2
      },
      {
        "id": "627a1d4d16742255657ead98",
        "uuid": "a7db5d4c-9bb4-56aa-a394-33d93a3a0b42",
        "areaName": "Big Bear North",
        "pathTokens": [
          "US",
          "California",
          "San Bernardino Mountains",
          "Big Bear Lake Area",
          "Big Bear North"
        ],
        "totalClimbs": 749,
        "density": 6.691435494637652
      },
      {
        "id": "627a1d4c16742255657e8a5d",
        "uuid": "198facc2-f25b-5ee9-a386-df4e3c4c5ee2",
        "areaName": "Shelf Road",
        "pathTokens": [
          "US",
          "Colorado",
          "Canon City",
          "Shelf Road"
        ],
        "totalClimbs": 1196,
        "density": 37.66317161369403
      },
      {
        "id": "627a1d4c16742255657ea429",
        "uuid": "fe5feef6-3d7a-5be3-ac07-5a27dec28b23",
        "areaName": "1 -  Lower Highway",
        "pathTokens": [
          "US",
          "Arizona",
          "Southern Arizona",
          "Mount Lemmon (Santa Catalina Mountains)",
          "Mount Lemmon (Catalina Highway)",
          "1 -  Lower Highway"
        ],
        "totalClimbs": 624,
        "density": 21.622356002983913
      },
      {
        "id": "627a1d4d16742255657eae61",
        "uuid": "cb88a652-f6f2-5e30-970a-938cef69ff0d",
        "areaName": "Big Bear City Area",
        "pathTokens": [
          "US",
          "California",
          "San Bernardino Mountains",
          "Big Bear Lake Area",
          "Big Bear North",
          "Big Bear City Area"
        ],
        "totalClimbs": 631,
        "density": 14.537411571640135
      },
      {
        "id": "627a1d4c16742255657e8b6b",
        "uuid": "3008c0fb-0ce5-525b-b50f-6155887d0597",
        "areaName": "South Platte",
        "pathTokens": [
          "US",
          "Colorado",
          "South Platte"
        ],
        "totalClimbs": 3019,
        "density": 0.7008395743127946
      },
      {
        "id": "627a1d4d16742255657eaf48",
        "uuid": "f76f23d7-14c6-5b25-8182-3930105e32ea",
        "areaName": "Holcomb Valley Pinnacles",
        "pathTokens": [
          "US",
          "California",
          "San Bernardino Mountains",
          "Big Bear Lake Area",
          "Big Bear North",
          "Big Bear City Area",
          "Holcomb Valley Pinnacles"
        ],
        "totalClimbs": 542,
        "density": 40.74576989127518
      },
      {
        "id": "627a1d4d16742255657eaf5a",
        "uuid": "57c59975-e374-5b92-9431-fd0751dede3c",
        "areaName": "Donner Summit",
        "pathTokens": [
          "US",
          "California",
          "Lake Tahoe",
          "I-80 Corridor",
          "Donner Summit"
        ],
        "totalClimbs": 402,
        "density": 45.51267080144036
      },
      {
        "id": "627a1d4d16742255657eafeb",
        "uuid": "e435466b-628d-5656-8782-09f8b0fa7212",
        "areaName": "Donner/Truckee Bouldering",
        "pathTokens": [
          "US",
          "California",
          "Lake Tahoe",
          "I-80 Corridor",
          "Donner/Truckee Bouldering"
        ],
        "totalClimbs": 430,
        "density": 0.9210170915152459
      },
      {
        "id": "627a1d4c16742255657e8cc8",
        "uuid": "100d5508-4531-5c61-b19e-fa666bc6229a",
        "areaName": "Devil's Head",
        "pathTokens": [
          "US",
          "Colorado",
          "South Platte",
          "Devil's Head"
        ],
        "totalClimbs": 601,
        "density": 29.42528732008078
      },
      {
        "id": "627a1d4c16742255657ea673",
        "uuid": "acd5e4e7-2972-5435-a237-4cea3dffe6cb",
        "areaName": "Queen Creek Canyon",
        "pathTokens": [
          "US",
          "Arizona",
          "Central Arizona",
          "Queen Creek Canyon"
        ],
        "totalClimbs": 922,
        "density": 20.23829291078724
      },
      {
        "id": "627a1d4c16742255657e8e6b",
        "uuid": "6cc0c3ef-2ec2-5348-8d10-2741c38624f2",
        "areaName": "Morrison/Evergreen/Littleton",
        "pathTokens": [
          "US",
          "Colorado",
          "Morrison/Evergreen/Littleton"
        ],
        "totalClimbs": 792,
        "density": 1.2362972157211376
      },
      {
        "id": "627a1d4c16742255657e8e7a",
        "uuid": "ebe9235e-a40c-5b97-b769-65db0bdd0cdc",
        "areaName": "Rifle",
        "pathTokens": [
          "US",
          "Colorado",
          "Rifle"
        ],
        "totalClimbs": 465,
        "density": 4.138091848516789
      },
      {
        "id": "627a1d4c16742255657e8e84",
        "uuid": "22dac198-10d8-5ebf-94d5-6e503a0753a0",
        "areaName": "Rifle Mountain Park",
        "pathTokens": [
          "US",
          "Colorado",
          "Rifle",
          "Rifle Mountain Park"
        ],
        "totalClimbs": 452,
        "density": 90.4
      },
      {
        "id": "627a1d4c16742255657e8ef1",
        "uuid": "1d93c24d-6b11-598e-ba18-80cc7121feb6",
        "areaName": "Alderfer/Three Sisters Park",
        "pathTokens": [
          "US",
          "Colorado",
          "Morrison/Evergreen/Littleton",
          "Alderfer/Three Sisters Park"
        ],
        "totalClimbs": 404,
        "density": 80.8
      },
      {
        "id": "627a1d4c16742255657e8fa5",
        "uuid": "74632cc0-a38c-534d-8344-0ada57f54a44",
        "areaName": "Lyons",
        "pathTokens": [
          "US",
          "Colorado",
          "Lyons"
        ],
        "totalClimbs": 710,
        "density": 1.2107562173452988
      },
      {
        "id": "627a1d4c16742255657e8fb6",
        "uuid": "1cfe9980-37c5-592d-9648-d6fc803c3824",
        "areaName": "Independence Pass",
        "pathTokens": [
          "US",
          "Colorado",
          "Independence Pass"
        ],
        "totalClimbs": 737,
        "density": 1.4103183295492778
      },
      {
        "id": "627a1d4c16742255657e8fc3",
        "uuid": "89eb0289-9906-5fed-8dbf-75620ff6ab2b",
        "areaName": "St. Vrain Canyons",
        "pathTokens": [
          "US",
          "Colorado",
          "Lyons",
          "St. Vrain Canyons"
        ],
        "totalClimbs": 654,
        "density": 2.421435621125763
      },
      {
        "id": "627a1d4c16742255657e8fc4",
        "uuid": "10f12d5c-d05a-52d0-ae46-729c528928e5",
        "areaName": "South Fork of St. Vrain Canyon",
        "pathTokens": [
          "US",
          "Colorado",
          "Lyons",
          "St. Vrain Canyons",
          "South Fork of St. Vrain Canyon"
        ],
        "totalClimbs": 478,
        "density": 9.807505182910297
      },
      {
        "id": "627a1d4c16742255657e8feb",
        "uuid": "4246501c-a558-5494-8fdc-ef635bbb8bbb",
        "areaName": "Unaweep Canyon",
        "pathTokens": [
          "US",
          "Colorado",
          "Grand Junction Area",
          "Unaweep Canyon"
        ],
        "totalClimbs": 2721,
        "density": 0.8519147362168905
      },
      {
        "id": "627a1d4c16742255657e8fec",
        "uuid": "b9b123a7-fbea-5dff-81ca-bb33975aa143",
        "areaName": "Nine Mile Hill",
        "pathTokens": [
          "US",
          "Colorado",
          "Grand Junction Area",
          "Unaweep Canyon",
          "Nine Mile Hill"
        ],
        "totalClimbs": 2212,
        "density": 34.34194508856694
      },
      {
        "id": "627a1d4c16742255657e8fef",
        "uuid": "f4c2e930-325e-56ce-850c-ca86bed85c98",
        "areaName": "Nine Mile Bouldering",
        "pathTokens": [
          "US",
          "Colorado",
          "Grand Junction Area",
          "Unaweep Canyon",
          "Nine Mile Hill",
          "Nine Mile Bouldering"
        ],
        "totalClimbs": 2142,
        "density": 33.25517467437178
      },
      {
        "id": "627a1d4d16742255657eb3a2",
        "uuid": "63a84574-0db2-5bec-975f-1d14f57aabe4",
        "areaName": "Castle Rock Area",
        "pathTokens": [
          "US",
          "California",
          "San Francisco Bay Area",
          "Castle Rock Area"
        ],
        "totalClimbs": 470,
        "density": 0.9283591463529253
      },
      {
        "id": "627a1d4d16742255657eb456",
        "uuid": "836c8d8f-a548-5fa7-b3ad-85af8b00988d",
        "areaName": "Tramway, The",
        "pathTokens": [
          "US",
          "California",
          "San Jacinto Mountains",
          "Tramway, The"
        ],
        "totalClimbs": 506,
        "density": 101.2
      },
      {
        "id": "627a1d4c16742255657e914e",
        "uuid": "12210cd6-f5dd-5222-b8be-e1811449c4b3",
        "areaName": "Mecca Boulder Area",
        "pathTokens": [
          "US",
          "Colorado",
          "Grand Junction Area",
          "Unaweep Canyon",
          "Nine Mile Hill",
          "Nine Mile Bouldering",
          "Mecca Boulder Area"
        ],
        "totalClimbs": 617,
        "density": 123.4
      },
      {
        "id": "627a1d4d16742255657eb576",
        "uuid": "58a4c1de-fc5b-5e0c-89ad-ab28ac59e4fe",
        "areaName": "Bishop Area",
        "pathTokens": [
          "US",
          "California",
          "Sierra Eastside",
          "Bishop Area"
        ],
        "totalClimbs": 2965,
        "density": 3.093354324383815
      },
      {
        "id": "627a1d4d16742255657eb590",
        "uuid": "4fb0d773-72c8-5105-9d28-790d95365d32",
        "areaName": "Pine Creek Canyon",
        "pathTokens": [
          "US",
          "California",
          "Sierra Eastside",
          "Bishop Area",
          "Pine Creek Canyon"
        ],
        "totalClimbs": 469,
        "density": 33.79508024319471
      },
      {
        "id": "627a1d4d16742255657eb5b0",
        "uuid": "0dde3658-d0f7-5305-8f32-e15b35086518",
        "areaName": "Owens River Gorge",
        "pathTokens": [
          "US",
          "California",
          "Sierra Eastside",
          "Bishop Area",
          "Owens River Gorge"
        ],
        "totalClimbs": 935,
        "density": 163.00587932951893
      },
      {
        "id": "627a1d4d16742255657eb678",
        "uuid": "2d851305-4237-55da-9626-16bb345bb0ad",
        "areaName": "June Lake Area",
        "pathTokens": [
          "US",
          "California",
          "Sierra Eastside",
          "June Lake Area"
        ],
        "totalClimbs": 438,
        "density": 2.5873415117335923
      },
      {
        "id": "627a1d4d16742255657eb67d",
        "uuid": "06f7203b-5a61-51d4-97e6-64b2d92b2669",
        "areaName": "Volcanic Tablelands (Happy/Sad Boulders)",
        "pathTokens": [
          "US",
          "California",
          "Sierra Eastside",
          "Bishop Area",
          "Volcanic Tablelands (Happy/Sad Boulders)"
        ],
        "totalClimbs": 735,
        "density": 19.27461658573978
      },
      {
        "id": "627a1d4d16742255657eb6b1",
        "uuid": "a2b7e130-46ff-5dd5-a8fb-abac68d65e1f",
        "areaName": "Buttermilk Country",
        "pathTokens": [
          "US",
          "California",
          "Sierra Eastside",
          "Bishop Area",
          "Buttermilk Country"
        ],
        "totalClimbs": 514,
        "density": 8.474665268621937
      },
      {
        "id": "627a1d4d16742255657eb6e2",
        "uuid": "c118fd6b-718a-585d-ad2f-04af278a0f55",
        "areaName": "Happy Boulders",
        "pathTokens": [
          "US",
          "California",
          "Sierra Eastside",
          "Bishop Area",
          "Volcanic Tablelands (Happy/Sad Boulders)",
          "Happy Boulders"
        ],
        "totalClimbs": 514,
        "density": 102.8
      },
      {
        "id": "627a1d4c16742255657e93e4",
        "uuid": "8b616c29-9f02-59ad-b4f6-1d23683e8913",
        "areaName": "Main Canyon: Unaweep Granite",
        "pathTokens": [
          "US",
          "Colorado",
          "Grand Junction Area",
          "Unaweep Canyon",
          "Main Canyon: Unaweep Granite"
        ],
        "totalClimbs": 447,
        "density": 2.311215579273836
      },
      {
        "id": "627a1d4d16742255657eb9d3",
        "uuid": "ce6ec458-d8d0-5439-aa24-025a8a8ec2e4",
        "areaName": "Tuolumne Meadows",
        "pathTokens": [
          "US",
          "California",
          "Yosemite National Park",
          "Tuolumne Meadows"
        ],
        "totalClimbs": 835,
        "density": 1.6928638090725718
      },
      {
        "id": "627a1d4c16742255657e9722",
        "uuid": "b34b81ad-639b-5002-8b62-fcc081599499",
        "areaName": "Golden",
        "pathTokens": [
          "US",
          "Colorado",
          "Golden"
        ],
        "totalClimbs": 2019,
        "density": 5.047496438360603
      },
      {
        "id": "627a1d4c16742255657e9736",
        "uuid": "e47011e8-0189-55d7-bf00-665ce3c108f4",
        "areaName": "Glenwood Springs",
        "pathTokens": [
          "US",
          "Colorado",
          "Glenwood Springs"
        ],
        "totalClimbs": 461,
        "density": 0.7643224164368067
      },
      {
        "id": "627a1d4c16742255657e97a1",
        "uuid": "279c5542-b8d6-5385-b9f0-746ce842d276",
        "areaName": "Big Thompson Canyon",
        "pathTokens": [
          "US",
          "Colorado",
          "Estes Park Valley",
          "Big Thompson Canyon"
        ],
        "totalClimbs": 514,
        "density": 5.767664376935835
      },
      {
        "id": "627a1d4c16742255657e97a9",
        "uuid": "f27f00b7-1968-5942-bffb-931b2cd00345",
        "areaName": "Poudre Canyon",
        "pathTokens": [
          "US",
          "Colorado",
          "Fort Collins",
          "Poudre Canyon"
        ],
        "totalClimbs": 1175,
        "density": 1.0198416231352574
      },
      {
        "id": "627a1d4d16742255657ebb0d",
        "uuid": "c8cedb1a-7848-5c2f-9bbd-235709d8626f",
        "areaName": "Apple Valley Area",
        "pathTokens": [
          "US",
          "California",
          "High Desert",
          "Apple Valley Area"
        ],
        "totalClimbs": 620,
        "density": 6.525673892255345
      },
      {
        "id": "627a1d4d16742255657ebb45",
        "uuid": "11c07a95-a49a-5858-a948-610be71fe850",
        "areaName": "New Jack City",
        "pathTokens": [
          "US",
          "California",
          "High Desert",
          "Barstow Area",
          "New Jack City"
        ],
        "totalClimbs": 420,
        "density": 77.8578547099444
      },
      {
        "id": "627a1d4c16742255657e97f6",
        "uuid": "8d173b36-c2fd-5494-aa98-344e8901142f",
        "areaName": "West of Rustic",
        "pathTokens": [
          "US",
          "Colorado",
          "Fort Collins",
          "Poudre Canyon",
          "West of Rustic"
        ],
        "totalClimbs": 457,
        "density": 3.083551454293104
      },
      {
        "id": "627a1d4d16742255657ebcfe",
        "uuid": "14a34046-d4ba-5064-b505-92d1514f96b6",
        "areaName": "Lower Merced River Canyon",
        "pathTokens": [
          "US",
          "California",
          "Yosemite National Park",
          "Yosemite Valley",
          "Lower Merced River Canyon"
        ],
        "totalClimbs": 428,
        "density": 4.389575227401434
      },
      {
        "id": "627a1d4d16742255657ebd50",
        "uuid": "5e3c95f8-ac0c-58d7-8278-934731f6453b",
        "areaName": "Valley North Side",
        "pathTokens": [
          "US",
          "California",
          "Yosemite National Park",
          "Yosemite Valley",
          "Valley North Side"
        ],
        "totalClimbs": 405,
        "density": 3.6780465718630766
      },
      {
        "id": "627a1d4d16742255657ebdb0",
        "uuid": "d1b5ac19-7ebe-5d62-8892-ff7f1b35564d",
        "areaName": "Riverside Area",
        "pathTokens": [
          "US",
          "California",
          "Inland Empire",
          "Riverside Area"
        ],
        "totalClimbs": 563,
        "density": 1.3439451461956908
      },
      {
        "id": "627a1d4c16742255657e9a9b",
        "uuid": "054defef-ef8b-511a-8dd3-3f5a56ac32eb",
        "areaName": "North Table Mountain/Golden Cliffs",
        "pathTokens": [
          "US",
          "Colorado",
          "Golden",
          "North Table Mountain/Golden Cliffs"
        ],
        "totalClimbs": 489,
        "density": 97.8
      },
      {
        "id": "627a1d4c16742255657e9aa6",
        "uuid": "8af5df63-9dd1-5fb2-9ef1-c3c3860494f5",
        "areaName": "Clear Creek Canyon",
        "pathTokens": [
          "US",
          "Colorado",
          "Golden",
          "Clear Creek Canyon"
        ],
        "totalClimbs": 1287,
        "density": 24.124649495119222
      },
      {
        "id": "627a1d4d16742255657ebf89",
        "uuid": "5af729d8-71a6-5bc2-a925-0f9adf369f4e",
        "areaName": "Central Joshua Tree",
        "pathTokens": [
          "US",
          "California",
          "Joshua Tree National Park",
          "Central Joshua Tree"
        ],
        "totalClimbs": 1068,
        "density": 29.41744805164451
      },
      {
        "id": "627a1d4d16742255657ebf8a",
        "uuid": "ff79bd0c-75a2-5388-a76e-f3683ec1e8d3",
        "areaName": "Echo Rock Area",
        "pathTokens": [
          "US",
          "California",
          "Joshua Tree National Park",
          "Central Joshua Tree",
          "Echo Rock Area"
        ],
        "totalClimbs": 423,
        "density": 84.6
      },
      {
        "id": "627a1d4d16742255657ebf99",
        "uuid": "11ba3258-8f86-56c3-a0c4-487335b5b388",
        "areaName": "Lost Horse Area",
        "pathTokens": [
          "US",
          "California",
          "Joshua Tree National Park",
          "Lost Horse Area"
        ],
        "totalClimbs": 635,
        "density": 85.61260557427113
      },
      {
        "id": "627a1d4d16742255657ebfac",
        "uuid": "60b73411-729d-5d2a-aa7f-7b448ebd9f93",
        "areaName": "Wonderland of Rocks",
        "pathTokens": [
          "US",
          "California",
          "Joshua Tree National Park",
          "Wonderland of Rocks"
        ],
        "totalClimbs": 635,
        "density": 17.275841160723157
      },
      {
        "id": "627a1d4d16742255657ebfb8",
        "uuid": "d1ca8e8d-6e70-5d21-8e0c-de4a0c325213",
        "areaName": "Sheep Pass Area",
        "pathTokens": [
          "US",
          "California",
          "Joshua Tree National Park",
          "Central Joshua Tree",
          "Sheep Pass Area"
        ],
        "totalClimbs": 422,
        "density": 23.853589185896876
      },
      {
        "id": "627a1d4d16742255657ec120",
        "uuid": "fc952fb1-cb91-5f1c-8512-ff5f0529534b",
        "areaName": "Pinto Basin",
        "pathTokens": [
          "US",
          "California",
          "Joshua Tree National Park",
          "Pinto Basin"
        ],
        "totalClimbs": 748,
        "density": 0.7238474155129134
      },
      {
        "id": "627a1d4d16742255657ec194",
        "uuid": "078f962c-2c44-5024-9ab7-c6cf3b9523f6",
        "areaName": "Indian Cove",
        "pathTokens": [
          "US",
          "California",
          "Joshua Tree National Park",
          "Indian Cove"
        ],
        "totalClimbs": 696,
        "density": 32.06982974533921
      },
      {
        "id": "627a1d4d16742255657ec1a2",
        "uuid": "bbf60ea4-d8bb-5949-a144-061868db1e5e",
        "areaName": "Hidden Valley Area",
        "pathTokens": [
          "US",
          "California",
          "Joshua Tree National Park",
          "Hidden Valley Area"
        ],
        "totalClimbs": 842,
        "density": 106.94964415398138
      },
      {
        "id": "627a1d4d16742255657ec532",
        "uuid": "216c65c1-a383-55c6-aabf-38bbc439532d",
        "areaName": "Running Springs Area",
        "pathTokens": [
          "US",
          "California",
          "San Bernardino Mountains",
          "Running Springs Area"
        ],
        "totalClimbs": 490,
        "density": 2.3240223423728477
      },
      {
        "id": "627a1d4d16742255657ec58f",
        "uuid": "2cc405d8-8121-585a-8161-68f9e17141c1",
        "areaName": "Hidden Valley Area Bouldering",
        "pathTokens": [
          "US",
          "California",
          "Joshua Tree National Park",
          "*Joshua Tree Bouldering*",
          "Hidden Valley Area Bouldering"
        ],
        "totalClimbs": 402,
        "density": 0.9473979015385798
      },
      {
        "id": "627a1d4d16742255657ec9ce",
        "uuid": "23df14e7-05e6-58d5-aad7-75a368e4ba4a",
        "areaName": "* Santa Barbara Bouldering",
        "pathTokens": [
          "US",
          "California",
          "Central Coast",
          "Santa Barbara",
          "* Santa Barbara Bouldering"
        ],
        "totalClimbs": 476,
        "density": 1.1916644531617897
      },
      {
        "id": "627a1db416742255657f342a",
        "uuid": "97c481c3-2f27-5119-acea-9d440f6a4603",
        "areaName": "Central Valley",
        "pathTokens": [
          "US",
          "Connecticut",
          "Central Valley"
        ],
        "totalClimbs": 441,
        "density": 1.053175244944965
      },
      {
        "id": "627a1e1316742255658085d5",
        "uuid": "ee49da5a-2539-54e5-b190-7ad5ece21316",
        "areaName": "Massacre Rocks",
        "pathTokens": [
          "US",
          "Idaho",
          "East Idaho",
          "Massacre Rocks"
        ],
        "totalClimbs": 475,
        "density": 95
      },
      {
        "id": "627a1e13167422556580869d",
        "uuid": "abbebc02-c1f8-57b0-bcba-ee8efb064ed2",
        "areaName": "City of Rocks",
        "pathTokens": [
          "US",
          "Idaho",
          "South Idaho",
          "City of Rocks"
        ],
        "totalClimbs": 564,
        "density": 16.641619621002697
      },
      {
        "id": "627a1e1b16742255658097e5",
        "uuid": "8bafd7e2-dec9-5ef5-b460-02b47362ceba",
        "areaName": "*Jackson Falls",
        "pathTokens": [
          "US",
          "Illinois",
          "*Jackson Falls"
        ],
        "totalClimbs": 528,
        "density": 105.6
      },
      {
        "id": "627a1e43167422556581275e",
        "uuid": "78da26bc-cd94-5ac8-8e1c-815f7f30a28b",
        "areaName": "Red River Gorge",
        "pathTokens": [
          "US",
          "Kentucky",
          "Red River Gorge"
        ],
        "totalClimbs": 2674,
        "density": 3.99087296130897
      },
      {
        "id": "627a1e431674225565812763",
        "uuid": "5a06ecdf-2665-546a-8d86-06b6146e26a9",
        "areaName": "Pendergrass-Murray Recreational Preserve (PMRP)",
        "pathTokens": [
          "US",
          "Kentucky",
          "Red River Gorge",
          "Pendergrass-Murray Recreational Preserve (PMRP)"
        ],
        "totalClimbs": 534,
        "density": 26.665800451699656
      },
      {
        "id": "627a1e431674225565812766",
        "uuid": "d51a127b-e771-5211-b1a9-bf5ad2703002",
        "areaName": "Northern Gorge",
        "pathTokens": [
          "US",
          "Kentucky",
          "Red River Gorge",
          "Northern Gorge"
        ],
        "totalClimbs": 573,
        "density": 2.555832122818841
      },
      {
        "id": "627a1e43167422556581280e",
        "uuid": "9a6de753-29c3-58be-8b9d-628ec15010fe",
        "areaName": "Muir Valley",
        "pathTokens": [
          "US",
          "Kentucky",
          "Red River Gorge",
          "Muir Valley"
        ],
        "totalClimbs": 428,
        "density": 85.6
      },
      {
        "id": "627a1e43167422556581284e",
        "uuid": "a2f96fb0-8daa-5d38-afea-f0ee2d5c7501",
        "areaName": "Miller Fork Recreational Preserve (MFRP)",
        "pathTokens": [
          "US",
          "Kentucky",
          "Red River Gorge",
          "Miller Fork Recreational Preserve (MFRP)"
        ],
        "totalClimbs": 460,
        "density": 92
      },
      {
        "id": "627a1e971674225565824d0d",
        "uuid": "2a40e704-cca6-5cd0-8b7d-404654e65186",
        "areaName": "Lynn Woods",
        "pathTokens": [
          "US",
          "Massachusetts",
          "North Shore",
          "Lynn Woods"
        ],
        "totalClimbs": 1290,
        "density": 2.716799374300875
      },
      {
        "id": "627a1e971674225565824f7d",
        "uuid": "25d55686-3cf3-5f91-a7d3-2ef4850930e1",
        "areaName": "Greater Lynn Woods Area",
        "pathTokens": [
          "US",
          "Massachusetts",
          "North Shore",
          "Lynn Woods",
          "Greater Lynn Woods Area"
        ],
        "totalClimbs": 546,
        "density": 1.1499011305180449
      },
      {
        "id": "627a1ebb167422556582c6ad",
        "uuid": "ec0de6c1-dc65-5419-8326-028ed274cf48",
        "areaName": "Duluth Area (Rock and Ice)",
        "pathTokens": [
          "US",
          "Minnesota",
          "Duluth Area (Rock and Ice)"
        ],
        "totalClimbs": 433,
        "density": 0.6196292319583832
      },
      {
        "id": "627a1ebb167422556582c6c1",
        "uuid": "63085c94-b228-52dd-919c-76692a9990de",
        "areaName": "Duluth Rock Climbs",
        "pathTokens": [
          "US",
          "Minnesota",
          "Duluth Area (Rock and Ice)",
          "Duluth Rock Climbs"
        ],
        "totalClimbs": 408,
        "density": 0.5860831004429055
      },
      {
        "id": "627a1f1d1674225565841b68",
        "uuid": "bea6bf11-de53-5046-a5b4-b89217b7e9bc",
        "areaName": "Red Rocks",
        "pathTokens": [
          "US",
          "Nevada",
          "Southern Nevada",
          "Red Rocks"
        ],
        "totalClimbs": 2980,
        "density": 13.828965201650078
      },
      {
        "id": "627a1f1d1674225565841c0a",
        "uuid": "37ff48e8-ef70-5be1-b9a3-8a7f154d75d5",
        "areaName": "* Red Rock Bouldering",
        "pathTokens": [
          "US",
          "Nevada",
          "Southern Nevada",
          "Red Rocks",
          "* Red Rock Bouldering"
        ],
        "totalClimbs": 606,
        "density": 3.3890848959552167
      },
      {
        "id": "627a1f2d16742255658448bb",
        "uuid": "fdf16fa4-e20a-5cda-8c1b-dad225df6dce",
        "areaName": "*Rumney",
        "pathTokens": [
          "US",
          "New Hampshire",
          "*Rumney"
        ],
        "totalClimbs": 1098,
        "density": 51.0596195485911
      },
      {
        "id": "627a1f2d16742255658448be",
        "uuid": "f472e63d-9089-5206-ab16-8385450ac7a4",
        "areaName": "*Pawtuckaway",
        "pathTokens": [
          "US",
          "New Hampshire",
          "*Pawtuckaway"
        ],
        "totalClimbs": 917,
        "density": 90.05279231624388
      },
      {
        "id": "627a1f831674225565858aae",
        "uuid": "3301509f-ad6b-5cf1-909e-db85df0082bb",
        "areaName": "Los Alamos & White Rock",
        "pathTokens": [
          "US",
          "New Mexico",
          "Los Alamos & White Rock"
        ],
        "totalClimbs": 549,
        "density": 2.2803018612380526
      },
      {
        "id": "627a1f831674225565858ab4",
        "uuid": "671e371a-61db-5214-840e-77ebd0ac59fa",
        "areaName": "Jemez Mountains and Jemez Valley",
        "pathTokens": [
          "US",
          "New Mexico",
          "Jemez Mountains and Jemez Valley"
        ],
        "totalClimbs": 766,
        "density": 1.3021482283888108
      },
      {
        "id": "627a1f831674225565858ac0",
        "uuid": "990a83a0-3905-5f0d-93da-c12bf15e29c9",
        "areaName": "Socorro Area",
        "pathTokens": [
          "US",
          "New Mexico",
          "Socorro Area"
        ],
        "totalClimbs": 404,
        "density": 0.652139634992628
      },
      {
        "id": "627a1f831674225565858b68",
        "uuid": "521794d7-5c00-56e4-8d33-25b56adc47e5",
        "areaName": "Box Climbing Areas, The",
        "pathTokens": [
          "US",
          "New Mexico",
          "Socorro Area",
          "Box Climbing Areas, The"
        ],
        "totalClimbs": 403,
        "density": 80.6
      },
      {
        "id": "627a1f831674225565858cb7",
        "uuid": "60af20ff-2a39-5a85-86f5-9582969e2458",
        "areaName": "Organ Mountains",
        "pathTokens": [
          "US",
          "New Mexico",
          "Las Cruces Area Climbing",
          "Organ Mountains"
        ],
        "totalClimbs": 459,
        "density": 4.187292590561073
      },
      {
        "id": "627a1f97167422556585cb74",
        "uuid": "80770603-5b32-5a9b-84e0-dd0c995fba3f",
        "areaName": "Powerlinez",
        "pathTokens": [
          "US",
          "New York",
          "Powerlinez"
        ],
        "totalClimbs": 675,
        "density": 135
      },
      {
        "id": "627a1f97167422556585cc89",
        "uuid": "14cd0edf-22b5-5cfe-881d-c4a21245b333",
        "areaName": "Gunks, The",
        "pathTokens": [
          "US",
          "New York",
          "Gunks, The"
        ],
        "totalClimbs": 1127,
        "density": 30.84207333835957
      },
      {
        "id": "627a1f97167422556585cc8e",
        "uuid": "3d71209f-36a0-528f-aa53-a7e476c10115",
        "areaName": "Trapps, The",
        "pathTokens": [
          "US",
          "New York",
          "Gunks, The",
          "Trapps, The"
        ],
        "totalClimbs": 493,
        "density": 98.6
      },
      {
        "id": "627a1fa4167422556585f593",
        "uuid": "501a5223-8516-5d16-95c8-d19da85584bd",
        "areaName": "Rumbling Bald",
        "pathTokens": [
          "US",
          "North Carolina",
          "1. Southern Mountains Region",
          "Rumbling Bald"
        ],
        "totalClimbs": 465,
        "density": 0.8171141123201255
      },
      {
        "id": "627a201e167422556587aa2b",
        "uuid": "f3c655b6-9c95-597f-aaa6-fd7d8a4865ec",
        "areaName": "Smith Rock",
        "pathTokens": [
          "US",
          "Oregon",
          "Central Oregon",
          "Smith Rock"
        ],
        "totalClimbs": 1229,
        "density": 127.33240646635645
      },
      {
        "id": "627a204916742255658831db",
        "uuid": "10f89d9c-9003-5a54-bad9-5849a525a2de",
        "areaName": "Rhode Island",
        "pathTokens": [
          "US",
          "Rhode Island"
        ],
        "totalClimbs": 1610,
        "density": 0.5319558307659191
      },
      {
        "id": "627a20491674225565883299",
        "uuid": "da04f374-e87e-512a-af4a-0dff8754db36",
        "areaName": "Lincoln Woods",
        "pathTokens": [
          "US",
          "Rhode Island",
          "Lincoln Woods"
        ],
        "totalClimbs": 897,
        "density": 179.4
      },
      {
        "id": "627a206f167422556588be78",
        "uuid": "72e16981-389a-5984-940d-40c1c28d0732",
        "areaName": "Spearfish Canyon",
        "pathTokens": [
          "US",
          "South Dakota",
          "Spearfish Canyon"
        ],
        "totalClimbs": 847,
        "density": 5.136481346290042
      },
      {
        "id": "627a206f167422556588be80",
        "uuid": "fcb9c76c-57ba-50f2-aa2c-1b574137f473",
        "areaName": "Needles Of Rushmore, The",
        "pathTokens": [
          "US",
          "South Dakota",
          "Needles Of Rushmore, The"
        ],
        "totalClimbs": 1270,
        "density": 1.7233649534297741
      },
      {
        "id": "627a206f167422556588be84",
        "uuid": "eb71723c-d454-5686-9f66-8bbd19c7143e",
        "areaName": "Custer State Park",
        "pathTokens": [
          "US",
          "South Dakota",
          "Custer State Park"
        ],
        "totalClimbs": 615,
        "density": 3.1487604411950962
      },
      {
        "id": "627a206f167422556588bf3f",
        "uuid": "3b48a6c3-f8e6-52f5-b57a-35a299fb1b7a",
        "areaName": "Mount Rushmore National Memorial",
        "pathTokens": [
          "US",
          "South Dakota",
          "Needles Of Rushmore, The",
          "Mount Rushmore National Memorial"
        ],
        "totalClimbs": 883,
        "density": 1.5120893783322966
      },
      {
        "id": "627a207c167422556588e502",
        "uuid": "2a6bddb9-e2a0-585c-91fa-29e712f07e0e",
        "areaName": "Obed & Clear Creek",
        "pathTokens": [
          "US",
          "Tennessee",
          "Obed & Clear Creek"
        ],
        "totalClimbs": 590,
        "density": 12.990252589743458
      },
      {
        "id": "627a20c616742255658a008c",
        "uuid": "457ea224-0d15-5f68-9d1e-2a153b89bc3b",
        "areaName": "Hueco Tanks",
        "pathTokens": [
          "US",
          "Texas",
          "Hueco Tanks"
        ],
        "totalClimbs": 646,
        "density": 2.1717537840776777
      },
      {
        "id": "627a20e216742255658a6a87",
        "uuid": "7e647943-f7a4-5fd8-bd0e-776f82e86c1b",
        "areaName": "Maple Canyon",
        "pathTokens": [
          "US",
          "Utah",
          "Central Utah",
          "Maple Canyon"
        ],
        "totalClimbs": 673,
        "density": 134.6
      },
      {
        "id": "627a20e216742255658a6a8b",
        "uuid": "2e946079-7cab-57dd-932a-ce00a2f6c801",
        "areaName": "Joe's Valley",
        "pathTokens": [
          "US",
          "Utah",
          "Central Utah",
          "Joe's Valley"
        ],
        "totalClimbs": 671,
        "density": 2.6236753015482357
      },
      {
        "id": "627a20e216742255658a6a92",
        "uuid": "e838736e-03de-5522-b170-850c7ffcb2ac",
        "areaName": "Central Wasatch",
        "pathTokens": [
          "US",
          "Utah",
          "Wasatch Range",
          "Central Wasatch"
        ],
        "totalClimbs": 3191,
        "density": 1.9319956935271536
      },
      {
        "id": "627a20e216742255658a6b7f",
        "uuid": "007f1fc1-3268-5660-b397-b7543d332216",
        "areaName": "Little Cottonwood Canyon",
        "pathTokens": [
          "US",
          "Utah",
          "Wasatch Range",
          "Central Wasatch",
          "Little Cottonwood Canyon"
        ],
        "totalClimbs": 1826,
        "density": 3.082827057119804
      },
      {
        "id": "627a20e216742255658a6b8c",
        "uuid": "26a193ca-cb5e-5423-8ead-6db185433cfb",
        "areaName": "Big Cottonwood Canyon",
        "pathTokens": [
          "US",
          "Utah",
          "Wasatch Range",
          "Central Wasatch",
          "Big Cottonwood Canyon"
        ],
        "totalClimbs": 917,
        "density": 5.512109488160405
      },
      {
        "id": "627a20e216742255658a6cb4",
        "uuid": "c6dbcb5f-af07-5552-b2a1-a98549545436",
        "areaName": "Boulders - Little Cottonwood",
        "pathTokens": [
          "US",
          "Utah",
          "Wasatch Range",
          "Central Wasatch",
          "Little Cottonwood Canyon",
          "Boulders - Little Cottonwood"
        ],
        "totalClimbs": 836,
        "density": 2.18544026117815
      },
      {
        "id": "627a20e216742255658a7283",
        "uuid": "f166e672-4a52-56d3-94f1-14c876feb670",
        "areaName": "Indian Creek",
        "pathTokens": [
          "US",
          "Utah",
          "Southeast Utah",
          "Indian Creek"
        ],
        "totalClimbs": 1501,
        "density": 2.106168061671424
      },
      {
        "id": "627a20e216742255658a73eb",
        "uuid": "a24448f6-6633-5c54-b897-6926136d491b",
        "areaName": "Ogden",
        "pathTokens": [
          "US",
          "Utah",
          "Wasatch Range",
          "Northern Wasatch",
          "Ogden"
        ],
        "totalClimbs": 436,
        "density": 1.9656777709349649
      },
      {
        "id": "627a20e216742255658a747c",
        "uuid": "0f0d1cb5-366f-59ca-93d4-ebb0b62da19b",
        "areaName": "Rock Canyon",
        "pathTokens": [
          "US",
          "Utah",
          "Wasatch Range",
          "Southern Wasatch",
          "Rock Canyon"
        ],
        "totalClimbs": 471,
        "density": 94.2
      },
      {
        "id": "627a210616742255658ad5ca",
        "uuid": "f90b510e-efcb-57b2-aad8-114f0cd564c0",
        "areaName": "Bolton Area",
        "pathTokens": [
          "US",
          "Vermont",
          "1. Northern Vermont",
          "Bolton Area"
        ],
        "totalClimbs": 492,
        "density": 10.203647814540695
      },
      {
        "id": "627a210f16742255658af498",
        "uuid": "522337f4-f041-5101-b2a3-4603eebbf4b4",
        "areaName": "Grayson Highlands State Park",
        "pathTokens": [
          "US",
          "Virginia",
          "Southwest Virginia (Appalachia)",
          "Grayson Highlands State Park"
        ],
        "totalClimbs": 1222,
        "density": 3.016931961988132
      },
      {
        "id": "627a213216742255658b6625",
        "uuid": "499c68c4-277c-5703-af05-7f254fb0751e",
        "areaName": "Spokane Area",
        "pathTokens": [
          "US",
          "Washington",
          "Northeast Corner & Spokane",
          "Spokane Area"
        ],
        "totalClimbs": 617,
        "density": 0.5120295377249925
      },
      {
        "id": "627a213216742255658b67b7",
        "uuid": "0bb1bb37-18ee-5769-974b-2b238388e482",
        "areaName": "Skykomish Valley",
        "pathTokens": [
          "US",
          "Washington",
          "Central-West Cascades & Seattle",
          "Skykomish Valley"
        ],
        "totalClimbs": 1418,
        "density": 0.7508654528911755
      },
      {
        "id": "627a213216742255658b67d2",
        "uuid": "78d3da65-5d54-5bff-981e-928711279d52",
        "areaName": "Exit 38",
        "pathTokens": [
          "US",
          "Washington",
          "Central-West Cascades & Seattle",
          "North Bend & Vicinity",
          "Exit 38"
        ],
        "totalClimbs": 472,
        "density": 32.38311846107077
      },
      {
        "id": "627a213216742255658b689b",
        "uuid": "a701bef6-2ff8-5c72-9aea-afe92f0bc5fa",
        "areaName": "Index",
        "pathTokens": [
          "US",
          "Washington",
          "Central-West Cascades & Seattle",
          "Skykomish Valley",
          "Index"
        ],
        "totalClimbs": 733,
        "density": 8.720413140587286
      },
      {
        "id": "627a213216742255658b6c68",
        "uuid": "c69b046c-cf9b-54e7-9eb6-ac9f013afbfa",
        "areaName": "Frenchman Coulee, AKA Vantage",
        "pathTokens": [
          "US",
          "Washington",
          "Central Region",
          "Frenchman Coulee, AKA Vantage"
        ],
        "totalClimbs": 584,
        "density": 103.96302480378493
      },
      {
        "id": "627a213216742255658b6c97",
        "uuid": "04e395a7-b62f-5055-b5c3-e0a7b724df28",
        "areaName": "Leavenworth",
        "pathTokens": [
          "US",
          "Washington",
          "Central-East Cascades, Wenatchee, & Leavenworth",
          "Leavenworth"
        ],
        "totalClimbs": 1560,
        "density": 3.1949086711061025
      },
      {
        "id": "627a213216742255658b6ca8",
        "uuid": "1a4b9fe5-403c-5a9c-b802-1d0ab5e68e1d",
        "areaName": "Icicle Creek",
        "pathTokens": [
          "US",
          "Washington",
          "Central-East Cascades, Wenatchee, & Leavenworth",
          "Leavenworth",
          "Icicle Creek"
        ],
        "totalClimbs": 1124,
        "density": 12.869810275355242
      },
      {
        "id": "627a213216742255658b6d2a",
        "uuid": "ec426459-bba7-541c-8411-63952095bef2",
        "areaName": "** Bouldering in Icicle Creek",
        "pathTokens": [
          "US",
          "Washington",
          "Central-East Cascades, Wenatchee, & Leavenworth",
          "Leavenworth",
          "Icicle Creek",
          "** Bouldering in Icicle Creek"
        ],
        "totalClimbs": 547,
        "density": 7.326146986023475
      },
      {
        "id": "627a214416742255658b9630",
        "uuid": "8a004a82-852f-54ab-ad77-bcbed7774cb5",
        "areaName": "New River Gorge, The",
        "pathTokens": [
          "US",
          "West Virginia",
          "New River Gorge, The"
        ],
        "totalClimbs": 1827,
        "density": 1.3492540516611085
      },
      {
        "id": "627a214416742255658b9633",
        "uuid": "859a8442-3fbd-542b-98fd-0eb6b3d2d762",
        "areaName": "New River Gorge Proper",
        "pathTokens": [
          "US",
          "West Virginia",
          "New River Gorge, The",
          "New River Gorge Proper"
        ],
        "totalClimbs": 1145,
        "density": 2.9983007582208434
      },
      {
        "id": "627a214416742255658b9729",
        "uuid": "dfd51586-7af2-59dc-bd58-455e2fd2e841",
        "areaName": "Meadow River Gorge",
        "pathTokens": [
          "US",
          "West Virginia",
          "New River Gorge, The",
          "Meadow River Gorge"
        ],
        "totalClimbs": 410,
        "density": 22.665426568115304
      },
      {
        "id": "627a214416742255658b97b2",
        "uuid": "cc8bc30a-6e39-5488-8dca-e8414e26a1cf",
        "areaName": "Coopers Rock State Forest",
        "pathTokens": [
          "US",
          "West Virginia",
          "Northern WV",
          "Coopers Rock State Forest"
        ],
        "totalClimbs": 571,
        "density": 48.7950586118236
      },
      {
        "id": "627a219616742255658cc904",
        "uuid": "8c8a16c4-3fea-5c7c-b93d-f7b4f32d7b62",
        "areaName": "Baraboo Range",
        "pathTokens": [
          "US",
          "Wisconsin",
          "Baraboo Range"
        ],
        "totalClimbs": 2661,
        "density": 2.44224564889671
      },
      {
        "id": "627a219616742255658cc922",
        "uuid": "bf4481e8-d698-5b5f-a46d-81f807c26d7d",
        "areaName": "Devil's Lake",
        "pathTokens": [
          "US",
          "Wisconsin",
          "Baraboo Range",
          "Devil's Lake"
        ],
        "totalClimbs": 2642,
        "density": 73.97661833382931
      },
      {
        "id": "627a219616742255658cc968",
        "uuid": "3f816201-d74f-56f0-b555-3a760031664b",
        "areaName": "Devil's Lake Bouldering",
        "pathTokens": [
          "US",
          "Wisconsin",
          "Baraboo Range",
          "Devil's Lake",
          "Devil's Lake Bouldering"
        ],
        "totalClimbs": 1438,
        "density": 40.26433654960127
      },
      {
        "id": "627a219616742255658cc985",
        "uuid": "441c580a-6a69-5d3b-8fef-1aae4780c5ab",
        "areaName": "West Bluff",
        "pathTokens": [
          "US",
          "Wisconsin",
          "Baraboo Range",
          "Devil's Lake",
          "Devil's Lake Bouldering",
          "West Bluff"
        ],
        "totalClimbs": 520,
        "density": 104
      },
      {
        "id": "627a219616742255658cc990",
        "uuid": "3a59331f-cabd-54cc-a09e-3b7c15009de3",
        "areaName": "East Bluff",
        "pathTokens": [
          "US",
          "Wisconsin",
          "Baraboo Range",
          "Devil's Lake",
          "Devil's Lake Bouldering",
          "East Bluff"
        ],
        "totalClimbs": 606,
        "density": 121.2
      },
      {
        "id": "627a21c716742255658d7dd5",
        "uuid": "183fb1aa-8d3f-5bf1-b176-049cf356e744",
        "areaName": "Vedauwoo",
        "pathTokens": [
          "US",
          "Wyoming",
          "Vedauwoo"
        ],
        "totalClimbs": 1110,
        "density": 2.6331900650441944
      },
      {
        "id": "627a21c716742255658d7dd9",
        "uuid": "9abad566-2113-587e-95a5-b3abcfaa28ac",
        "areaName": "Ten Sleep Canyon",
        "pathTokens": [
          "US",
          "Wyoming",
          "Ten Sleep Canyon"
        ],
        "totalClimbs": 800,
        "density": 8.264803522709137
      },
      {
        "id": "627a21c716742255658d7f5c",
        "uuid": "b1166235-3328-5537-b5ed-92f406ea8495",
        "areaName": "Lander Area",
        "pathTokens": [
          "US",
          "Wyoming",
          "Lander Area"
        ],
        "totalClimbs": 1234,
        "density": 0.8747839883098073
      },
      {
        "id": "627a21c716742255658d7f70",
        "uuid": "90a197ac-28d0-5afa-9953-e56d25d2af21",
        "areaName": "Sinks Canyon",
        "pathTokens": [
          "US",
          "Wyoming",
          "Lander Area",
          "Sinks Canyon"
        ],
        "totalClimbs": 717,
        "density": 10.185370680057423
      }
    ]
ET.register_namespace('',"http://www.sitemaps.org/schemas/sitemap/0.9")

tree = ET.parse('sitemap.xml')

root = tree.getroot()

for area in areas:
    urlEle = ET.SubElement(root, 'url')
    locEle = ET.SubElement(urlEle, 'loc')
    locEle.text = f'https://tacos.openbeta.io/areas/{area["uuid"]}'



b_xml = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")

with open("sitemap.xml", "w") as f:
    f.write(b_xml)
