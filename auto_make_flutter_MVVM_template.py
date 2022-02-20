from tkinter import filedialog
import os
dir = ''
print("""
The program helps your making flutter program files which are written with MVVM and riverpod.
""")
input("Please select the folder that you want to make a folder which includes the promram files after type enter key:")
fld = filedialog.askdirectory(initialdir = dir) 

if fld=="":
    print("You tapped the cancel button!")
    exit()

widgetname=input("Please type the widget name that you want to make:")
#check
if (not widgetname.isalpha())or(not list(widgetname)[0].isupper()):
    print("You should name the widget following what written in the below link's article \n https://dart-lang.github.io/linter/lints/non_constant_identifier_names.html \n Please try again!")
    exit()
namelist=list(widgetname)
namelist[0]=namelist[0].lower()
namename="".join(namelist)

namelist=list(namename)
namelist=" ".join(namelist)
namelist=list(namelist)

for i in range(len(namelist)):
    if namelist[i].isupper():
        namelist[i-1]="_"
namelist=[i for i in namelist if i != " "]
foldername="".join(namelist).lower()

print("prosessing")
def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)

#view
save_file_at_dir(fld+"/"+foldername, 'view.dart', """

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'view_model.dart';

class """+widgetname+""" extends ConsumerStatefulWidget {
  const """+widgetname+"""({Key? key}) : super(key: key);

  @override
  ConsumerState createState() => _"""+widgetname+"""State();
}

class _"""+widgetname+"""State extends ConsumerState<"""+widgetname+"""> {
  final logic = """+widgetname+"""ViewModel();
  @override
  void initState() {
    super.initState();
    logic.setRef(ref);
  }

  @override
  Widget build(BuildContext context) {
    return Container();
  }
}

""")
#view_model
save_file_at_dir(fld+"/"+foldername, 'view_model.dart', """

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'logic.dart';
import 'data/data.dart';
class """+widgetname+"""ViewModel {
  late WidgetRef _ref;
  void setRef(WidgetRef ref) {
    _ref = ref;
  }

  """+widgetname+"""Data get _data => _ref.watch("""+namename+"""Provider);

  """+widgetname+"""Logic get _logic => _ref.read("""+namename+"""Provider.notifier);
}

""")
#logic
save_file_at_dir(fld+"/"+foldername, 'logic.dart', """

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'data/data.dart';

final """+namename+"""Provider =
    StateNotifierProvider.autoDispose<"""+widgetname+"""Logic, """+widgetname+"""Data>(
        (_) {
  return """+widgetname+"""Logic("""+widgetname+"""Data(title: ""));
});

class """+widgetname+"""Logic extends StateNotifier<"""+widgetname+"""Data> {
  """+widgetname+"""Logic("""+widgetname+"""Data state) : super(state);
}

""")
#data
save_file_at_dir(fld+"/"+foldername+"/data", 'data.dart', """

import 'package:freezed_annotation/freezed_annotation.dart';
import 'package:flutter/foundation.dart';
part 'data.freezed.dart';

@freezed
class """+widgetname+"""Data with _$"""+widgetname+"""Data {
  const factory """+widgetname+"""Data({
    required String title,
  }) = _"""+widgetname+"""Data;
}

""")
print("All done!")