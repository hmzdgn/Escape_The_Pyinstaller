from os import system, path
fn = input("File Name: ")

if fn[-4:] != ".exe":
    fn = fn + ".exe"

if not path.isfile(".\\"+fn):
    print("Wrong file name!")
    input("-> Press Enter For Exit <-\n")
    exit()

system(f"python signer.py -s sign.exe_sig -t {fn}")
print("\nNote: Signed with default sign (Philandro Software)")

# if not path.isfile(".\\new_"+fn):
#     system(f"ren {fn}_signed new_{fn}")
# else:
#     system(f"ren {fn}_signed new_{fn}")

input("\n-> Press Enter For Exit <-\n")