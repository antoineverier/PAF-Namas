//
//  DataView.swift
//  NAMAS
//
//  Created by Antoine Verier on 26/06/2023.
//

import SwiftUI

struct DataView: View {
    var body: some View {
        NavigationView {
            List(Data.list, id:\.id){
                data in DataItemView(data: data)
            }.listStyle(PlainListStyle()).navigationTitle("Photos des patients")
                .background(Color.black)
                .foregroundColor(Color.indigo)
        }
    }
}

struct DataItemView: View {
    let data : Data
    var body: some View {
        ZStack {
            Color.white.cornerRadius(8)
            HStack {
                image
                info
            }
            .padding()
            
        }
        .shadow(color: Color.black.opacity(0.2), radius: 5, x:0, y:2)
    }
}

private extension DataItemView{
    var image : some View {
        Image(data.image)
            .resizable()
            .scaledToFit()
            .frame(width: 162, height: 100)
    }
    var info : some View{
        VStack(alignment: .leading, spacing: 5) {
            Text(data.name)
                .font(.headline)
                .lineLimit(2)
                .foregroundColor(Color.indigo)
            Text(data.date)
                .font(.subheadline)
                .lineLimit(2)
                .foregroundColor(Color.black)
        }
    }
}

struct DataView_Previews: PreviewProvider {
    static var previews: some View {
        DataView()
    }
}
