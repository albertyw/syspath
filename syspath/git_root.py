from .syspath import append_git_root


path = append_git_root(index=5)

if __name__ == "__main__":
    print(path)
