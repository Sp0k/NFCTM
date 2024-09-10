import { StatusBar } from "expo-status-bar";
import { StyleSheet, Text, View } from "react-native";
import tw from "twrnc";

export default function App() {
  return (
    <View style={tw`justify-center flex flex-1 items-center`}>
      <Text style={tw`text-2xl font-bold`}>NFCTM</Text>
      <StatusBar style="auto" />
    </View>
  );
}
