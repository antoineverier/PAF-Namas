//
//  ContentView.swift
//  NAMAS
//
//  Created by Antoine Verier on 26/06/2023.
//

import SwiftUI

struct ContentView: View {
    
    var data : Data
    
    @State private var add = false
    var body: some View {
        NavigationView{
            VStack {
                Image("LogoNAMAS")
                    .resizable()
                    .padding(.leading, 0.0)
                    .scaledToFit()
                
                NavigationLink(
                    destination: AddImage(),
                    label: {
                        Label (
                            title: { Text("Ajouter des images").fontWeight(.semibold).font(.title)               },
                            icon: {Image(systemName: "camera").font(.title)
                            }
                        )
                    }).buttonStyle(GradientBackgroundStyle())
                
                NavigationLink(
                    destination: DataView(),
                    label: {
                        Label (
                            title: { Text("Consulter un médecin").fontWeight(.semibold).font(.title)               },
                            icon: {Image(systemName: "pills.fill").font(.title)
                            }
                        )
                    }).buttonStyle(GradientBackgroundStyle())
                
                NavigationLink(
                    destination: DataView(),
                    label: {
                        Label (
                            title: { Text("Consulter les images").fontWeight(.semibold).font(.title)               },
                            icon: {Image(systemName: "photo").font(.title)
                            }
                        )
                    }).buttonStyle(GradientBackgroundStyle())
    
                Spacer()
            }.background(Color.white)
        }
    }
}

struct GradientBackgroundStyle : ButtonStyle {
    func makeBody(configuration: Self.Configuration) -> some View {
        configuration.label
            .padding()
            .background(LinearGradient(gradient: Gradient(colors:[Color.indigo, Color("Black")]), startPoint: .leading, endPoint: .trailing))
            .cornerRadius(40.0)
            .foregroundColor(Color.white)
            .shadow(color: .gray, radius: 20.0, x : 20.0, y : 10.0)
            .scaleEffect(configuration.isPressed ? 0.9 : 1.0)
    }
}

struct AddImage_Previews: PreviewProvider {
    static var previews: some View {
        ContentView(data : Data.list[0])
    }
}

