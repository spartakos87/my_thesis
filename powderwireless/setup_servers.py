import os

if __name__ == '__main__':
    link_img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-67FFQJYGDA0mklORazEaP1O1AulxO816mwfJaEm69A0BgH6ShQ"
    # Download the given jpg, which is located in link_img url and rename it to download.jpg
    get_it = "wget -cO - "+link_img+" > download.jpg"
    create_folder = "mkdir foo"
    mv_downimg_tofoo = "mv download.jpg foo/"
    cd_folder = "cd foo"
    run_server = "python -m SimpleHTTPServer 1313"
    os.system(get_it)
    os.system(create_folder)
    os.system(mv_downimg_tofoo)
    os.system(cd_folder)
    os.system(run_server)
