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
        child: Text("The rules for this game are pretty simple"),
	      child: Text("• Newbie project created in react"),
	      child: Text("• React is only for professional web developers"),
	      child: Text("• only for fun"),
      ),
    );
  }
}
