//
//  NAMASApp.swift
//  NAMAS
//
//  Created by Antoine Verier on 26/06/2023.
//
import FirebaseCore


class AppDelegate: NSObject, UIApplicationDelegate {
  func application(_ application: UIApplication,
                   didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    FirebaseApp.configure()

    return true
  }

}
import SwiftUI

@main
struct NAMASApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate
     
    var body: some Scene {
        WindowGroup {
            ContentView(data : Data.list[0])
        }
    }
}

