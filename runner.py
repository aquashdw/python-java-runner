import os
import subprocess


def run_java(java_class, packages: list = None):
    command = "java "
    if packages is not None:
        package_str = "-cp "
        for package in packages:
            package_str += str(package).strip() + "/"
        command += package_str[:-1] + " "
    command += java_class

    subprocess.run(command, shell=True)


if __name__ == '__main__':
    create = True
    test_file = "Main.java"
    test_classfile = os.path.splitext(test_file)[0] + ".class"
    test_packages = test_file.split("/")[:-1] if "/" in test_file else None
    test_classname = test_classfile.split(".")[0]
    if test_packages:
        test_classname = test_classname.split("/")[-1]

    print(test_file)
    print(test_packages)
    print(test_classfile)
    print(test_classname)

    if create:
        if test_packages:
            os.makedirs(os.path.dirname(test_file), exist_ok=True)
        with open(test_file, "w") as f:
            f.write("""
            public class Main {
                public static void main(String[] args) {
                    System.out.println("Hello World!");
                }
            }
            """)
    subprocess.run(f"javac {test_file}", shell=True)
    run_java(test_classname, test_packages)
    os.remove(test_classfile)
    os.remove(test_file)
