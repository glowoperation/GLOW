import 'package:flutter/material.dart';
import 'router.dart';
import 'core/theme/app_theme.dart';

class GlowApp extends StatelessWidget {
  const GlowApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      debugShowCheckedModeBanner: false,
      title: 'GLOW',
      theme: AppTheme.lightTheme,
      routerConfig: appRouter,
    );
  }
}