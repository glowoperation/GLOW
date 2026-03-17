import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import 'features/home/pages/home_page.dart';

final GoRouter appRouter = GoRouter(
  initialLocation: '/home',
  routes: <RouteBase>[
    GoRoute(
      path: '/home',
      builder: (BuildContext context, GoRouterState state) {
        return const HomePage();
      },
    ),
  ],
);