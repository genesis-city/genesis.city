# genesis.city
Decentraland map.

![image](https://user-images.githubusercontent.com/287189/154358783-952b2693-083a-4afa-a0b4-c1f8cece6bdc.png)


For the mapper script, see https://github.com/maraoz/unity-renderer/blob/master/unity-renderer/Assets/Scripts/MapperCamera.cs

# API Docs

Retrieve individual parcel images from Genesis City Map.
Access a specific parcel image by making a GET request to the following URL format:

https://genesis.city/api/v1/land/{x-coordinate},{y-coordinate}.jpg

For example:
https://genesis.city/api/v1/land/137,-145.jpg
