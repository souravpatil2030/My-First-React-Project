import 'package:flutter/material.dart';

class RulesPage extends StatefulWidget {
  @override
  _RulesPageState createState() => _RulesPageState();
}

class _RulesPageState extends State<RulesPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Scratch and Win"),
      ),
      body: Center(
        child: Text("The rules for this app are pretty simple"),
	      child: Text("• one user at a time"),
	      child: Text("• react app to be used for professionals only"),
	      child: Text("• Do not use it as betting game play only for fun"),
      ),
    );
  }
}
