# stencilinator

This inator takes any picture available and converts it into a stencil which you can use on a pumpkin for carving! I made this code to provide a quick and dirty way to take an image which didn't have a readily available stencil and make a close approximation.

It will prompt you for three values, where the image is located (can be local or on the internet, just provide the whole address), what the name of the output image you want should be, and then the "Sigma" level.

Sigma is very much "nerd stuff", but in general, the higher the sigma, the higher the detail of the "stencil", however it takes more time to process. Typically, the less detailed your starting image is, the lower your sigma needs to be. Type in an integer value between 1 and however high you can count (or the upper limit of 32 bit values, whichever is first).

You will then be presented with what the image looks like, and then once you close the viewer, it will save to your specified location.

I've had some difficulties with the saving process on Macs, but if all else fails you can have it use the local directory if you simply specify the name of the file you wish to create without an absolute path.
