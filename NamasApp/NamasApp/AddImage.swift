//
//  AddImage.swift
//  NAMAS
//
//  Created by Antoine Verier on 26/06/2023.
//

import SwiftUI
import AVFoundation
import Photos

struct AddImage: View {
    
    @State private var date2 = ""
    @State private var nameUser = ""
    @State private var isShowingImagePicker = false
    @State private var capturedImage: UIImage?
    
    var body: some View {
        VStack {
            if let imagetaken = capturedImage {
                Image(uiImage: imagetaken)
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .padding()
                

                TextField("Date format ANNÉE-MOIS-JOUR", text: $date2)
                TextField("Name", text: $nameUser )
                Button("Ajouter la photo") {
                    let newData = Data(name: nameUser, date: date2, image: imagetaken.description)
                    print(newData)
                }.padding()
                    .background(Color.blue)
                    .foregroundColor(Color.white)
                    .cornerRadius(10)
                
            } else {
                Button(action: {
                    isShowingImagePicker = true
                }) {
                    Text("Ouvrir l'appareil photo")
                        .padding()
                        .background(Color.blue)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                }
                .sheet(isPresented: $isShowingImagePicker) {
                    ImagePickerView(capturedImage: $capturedImage)
                }
            }
        }
    }
}

struct ImagePickerView: UIViewControllerRepresentable {
    @Environment(\.presentationMode) var presentationMode
    @Binding var capturedImage: UIImage?
    
    func makeUIViewController(context: Context) -> UIImagePickerController {
        let imagePicker = UIImagePickerController()
        imagePicker.sourceType = .camera
        imagePicker.delegate = context.coordinator
        return imagePicker
    }
    
    func updateUIViewController(_ uiViewController: UIImagePickerController, context: Context) {}
    
    func makeCoordinator() -> Coordinator {
        Coordinator(capturedImage: $capturedImage, presentationMode: presentationMode)
    }
    
    class Coordinator: NSObject, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
        @Binding var capturedImage: UIImage?
        var presentationMode: Binding<PresentationMode>
        
        init(capturedImage: Binding<UIImage?>, presentationMode: Binding<PresentationMode>) {
            _capturedImage = capturedImage
            self.presentationMode = presentationMode
        }
        
        func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
            if let image = info[.originalImage] as? UIImage {
                capturedImage = image
                saveImageToPhotoLibrary(image)
            }
            
            presentationMode.wrappedValue.dismiss()
        }
        
        func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
            presentationMode.wrappedValue.dismiss()
        }
        
        func saveImageToPhotoLibrary(_ image: UIImage) {
            PHPhotoLibrary.requestAuthorization { status in
                guard status == .authorized else {
                    // Handle denied authorization
                    return
                }
                
                PHPhotoLibrary.shared().performChanges {
                    PHAssetChangeRequest.creationRequestForAsset(from: image)
                } completionHandler: { success, error in
                    if let error = error {
                        // Handle save error
                        print("Error saving image to photo library: \(error.localizedDescription)")
                    } else {
                        // Handle save success
                        print("Image saved to photo library successfully.")
                    }
                }
            }
        }
    }
}

struct ImagePickerView_Previews: PreviewProvider {
    static var previews: some View {
        AddImage()
    }
}
