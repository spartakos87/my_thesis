import os

if __name__ == '__main__':
    link_img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-67FFQJYGDA0mklORazEaP1O1AulxO816mwfJaEm69A0BgH6ShQ"
    get_it = "wget "+link_img
    creat_and_cd_folder = "mkdir foo && cd foo"
    run_server = "python -m SimpleHTTPServer 1313"
