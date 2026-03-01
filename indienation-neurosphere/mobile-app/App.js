import React, { useState, useEffect } from 'react';
import { View, Text, Image, TextInput, TouchableOpacity, ScrollView, StyleSheet, StatusBar } from 'react-native';

export default function App() {
  const [fase, setFase] = useState('splash'); 
  const [userData, setUserData] = useState({ iid: 'IID-021-0000000023', luv: 0, aura: 'Emerald Green' });

  useEffect(() => {
    if (fase === 'splash') {
      setTimeout(() => setFase('signup'), 3000);
    }
  }, [fase]);

  const handleSignUp = () => {
    setFase('dashboard');
  };

  const handleLogout = () => {
    setFase('signup');
  };

  if (fase === 'splash') {
    return (
      <View style={styles.containerAbyss}>
        <StatusBar barStyle="light-content" />
        <Text style={styles.title}>NEUROSPHERE</Text>
        <View style={styles.auraCircle} />
        <Text style={styles.subtitle}>Digital Sovereignty for 10 Billion People</Text>
      </View>
    );
  }

  if (fase === 'signup') {
    return (
      <View style={styles.container}>
        <Text style={styles.label}>ENTER YOUR IID</Text>
        <TextInput 
          style={styles.input} 
          placeholder="IID-021-XXXXXXXX" 
          placeholderTextColor="#333" 
          autoCapitalize="characters"
        />
        <TouchableOpacity style={styles.btnGold} onPress={handleSignUp}>
          <Text style={styles.btnText}>ACTIVATE IDENTITY</Text>
        </TouchableOpacity>
      </View>
    );
  }

  return (
    <ScrollView style={styles.dashboard}>
      <StatusBar barStyle="light-content" />
      <View style={styles.header}>
        <Text style={styles.auraTitle}>RANK: {userData.aura}</Text>
        <Text style={styles.iidText}>{userData.iid}</Text>
      </View>

      <View style={styles.statsCard}>
        <Text style={styles.statLabel}>ANCHOR VALUE</Text>
        <Text style={styles.statValue}>€100,000</Text>
        <Text style={styles.verifiedText}>STATUS: VERIFIED BY NEUROSPHERE</Text>
      </View>

      <View style={styles.tmContainer}>
        <Text style={styles.tmLabel}>Total TM (Technology Money)</Text>
        <View style={styles.tmDetail}>
           <Text style={styles.tmText}>ENPE: 1,000,000</Text>
           <Text style={styles.tmText}>LUV: 299</Text>
           <Text style={styles.tmText}>IND-EUR: 0.00</Text>
        </View>
      </View>

      <TouchableOpacity style={styles.btnLogout} onPress={handleLogout}>
        <Text style={styles.logoutText}>SECURE LOGOUT</Text>
      </TouchableOpacity>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  containerAbyss: { flex: 1, backgroundColor: '#000', justifyContent: 'center', alignItems: 'center' },
  container: { flex: 1, backgroundColor: '#050505', padding: 30, justifyContent: 'center' },
  dashboard: { flex: 1, backgroundColor: '#000', padding: 25 },
  title: { color: '#FFD700', fontSize: 35, fontWeight: 'bold', letterSpacing: 8 },
  subtitle: { color: '#444', marginTop: 20, fontSize: 12 },
  auraCircle: { width: 100, height: 100, borderRadius: 50, borderWeight: 2, borderColor: '#00ff88', marginTop: 30, backgroundColor: 'rgba(0, 255, 136, 0.1)' },
  label: { color: '#FFD700', fontSize: 14, marginBottom: 10, letterSpacing: 2 },
  input: { borderBottomWidth: 1, borderColor: '#FFD700', color: '#fff', marginBottom: 40, fontSize: 20, paddingVertical: 10 },
  btnGold: { backgroundColor: '#FFD700', padding: 18, borderRadius: 2, alignItems: 'center', shadowColor: '#FFD700', shadowOpacity: 0.5 },
  btnText: { fontWeight: 'bold', color: '#000', letterSpacing: 1 },
  header: { marginTop: 40, marginBottom: 30 },
  auraTitle: { color: '#00ff88', fontSize: 18, fontWeight: 'bold' },
  iidText: { color: '#fff', fontSize: 24, fontWeight: 'bold' },
  statsCard: { backgroundColor: '#111', padding: 25, borderRadius: 15, borderLeftWidth: 5, borderLeftColor: '#FFD700' },
  statLabel: { color: '#888', fontSize: 12, letterSpacing: 1 },
  statValue: { color: '#fff', fontSize: 32, fontWeight: 'bold', marginVertical: 5 },
  verifiedText: { color: '#00ff88', fontSize: 10, fontWeight: 'bold' },
  tmContainer: { marginTop: 30, padding: 20, backgroundColor: '#0a0a0a', borderRadius: 10 },
  tmLabel: { color: '#FFD700', marginBottom: 10 },
  tmText: { color: '#fff', fontSize: 14, marginBottom: 5 },
  btnLogout: { marginTop: 60, padding: 20, borderTopWidth: 0.5, borderColor: '#333', alignItems: 'center' },
  logoutText: { color: '#ff4444', fontSize: 14, fontWeight: 'bold' }
});
